from bs4 import BeautifulSoup
import requests
import json
import time


#TODO: Replace with async reqs to speed up fetching data

BASE_URL = 'https://howlongtobeat.com/search_results?page='
DATA = {
        'queryString': '',
        't': 'games',
        'sorthead': 'popular',
        'sortd': 'Normal Order',
        'plat': '',
        'length_type': 'main',
        'length_min': '',
        'length_max': '',
        'v': '',
        'f': '',
        'g': '',
        'detail': '',
        'randomize': '0'}
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
CONNECT_PAUSE = 5
game_times = []

def get_pg_num() -> int:
    r = requests.post(f'{BASE_URL}1', headers={'User-Agent':USER_AGENT}, data=DATA)
    soup = BeautifulSoup(r.text, features='html5lib')

    #the bar that includes the page numbers
    bar = soup.find('h2', {'class':'in back_secondary shadow_box right', 
                    'style':'margin-top:10px;'})
    
    pg_nums = bar.find_all('span', {'class' : 'search_list_page back_secondary shadow_box'})
    last_pg_num = pg_nums[-1].get_text()
    return int(last_pg_num)


def all_pages():
    for pg_num in range(1, get_pg_num()+1):
        try:
            r = requests.post(f'{BASE_URL}{pg_num}', headers={'User-Agent':USER_AGENT}, data=DATA)
        except ConnectionError:
            print(f"There was a connection error. Restarting connection in {CONNECT_PAUSE} secs.")
            time.sleep(CONNECT_PAUSE)

        pg_soup = BeautifulSoup(r.text, features='html5lib')
        
        games = pg_soup.find_all('li', {'class' : 'back_darkish'})
        for game in games:
            game_times.append(get_game_data(game))

        #rewrite the file every loop (cant append because it wouldn't work with json syntax)
        with open(f'time.json', 'w') as f:
            json.dump(game_times, f)
        print(f'saved to file {pg_num}')


def get_game_data(game:BeautifulSoup)->dict:
    
        game_dict = {}    
        game_title_tag = game.find('a', {'class':'text_white'})
        
        game_dict['name'] = game_title_tag.get_text()
        game_dict['url'] = game_title_tag['href']
        
        try:
            hrs_list = game.find('div', {'class':'search_list_details_block'}).find_all('div')
        except AttributeError:
            #Some games have no data available on their play time
            return game_dict

        #The game included an outer div
        if len(hrs_list) % 2 != 0:
            hrs_list.pop(0)

        #in hrs_list, the even(0,2,4) indices have the header(main
        #story time, completionist time), and odd indeces have the data for the
        #header that came before them
        for item_num in range(0, len(hrs_list), 2):
            field_name = hrs_list[item_num].get_text()
            game_dict[field_name + ' time'] = hrs_list[item_num+1].get_text()
            
            #The class attr is differnt based on number of players that voted
            game_dict[field_name + ' tag info'] = ' '.join(hrs_list[item_num+1]['class'])

        print(game_dict['name'], 'added to json obj')
        return game_dict

all_pages()