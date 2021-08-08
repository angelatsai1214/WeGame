import json
import pandas as pd
from typing import List, Dict
from copy import deepcopy
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



GAME_DATA_PATH = "\dataClean\games02.json"
WEGAME_GAMES_DATA_PATH = "\dataClean\SampleWeGameDevs02.json"
USER_DATA_PATH = "\dataClean\SampleSteamUser.json"
#OUTPUT_RECCOMMENDATIOS_FILE = "\dataClean\SampleReccs.json"


#def save_data(reccs:Dict):
#    with open(OUTPUT_RECCOMMENDATIOS_FILE, "w") as file:
#        json.dump(reccs, file)


def find_game_info_in_db(game_name:str, db:pd.DataFrame)->pd.Series:
    result = db.index[db["name"] == game_name].tolist()
    try:
        return db.iloc[result[0]]
    except IndexError:
        return None


def make_soup(x):
    final_str = ""
    if x['genres'] is not None:
        final_str = final_str + ' '.join(str(i) for i in x['genres']) + " "
    if x['game_modes'] is not None:
        final_str = final_str + ' '.join(str(i) for i in x['game_modes']) + " "
    if x['player_perspectives'] is not None:
        final_str = final_str + ' '.join(str(i) for i in x['player_perspectives']) + " "
    if x['themes'] is not None:
        final_str = final_str + ' '.join(str(i) for i in x['themes']) + " "

    return final_str.strip()


def preprocess_data(external_games_data_file, internal_games_data_file):
    """Process data and make it ready for use
    @external_games_data_file: The file path for the file that stores all the data on
    the video games from external sources like steam or playstation store.
    Has many data fields and is fetched from igdb's API, using igdb.py
    @internal_games_data_file: The file path for the file that stores all the data on games
    submitted by indie devs of our platform"""
    outgames = pd.read_json(f"{os.getcwd()}{external_games_data_file}")
    wegame = pd.read_json(f"{os.getcwd()}{internal_games_data_file}")
    
    #Deepcopy the subset of dfs that are important and continue working with those
    fields = ["name", "game_modes", "player_perspectives", "genres", "themes"]
    outgames_c = deepcopy(outgames[fields])
    wegame_c = deepcopy(wegame[fields])
    outgames_c = outgames_c[:40000]
    #print(outgames_c.shape)
    
    #Add a weGame column for confirming the source
    outgames_c["WeGame"] = [False for _ in range(len(outgames_c))]
    wegame_c["WeGame"] = [True for _ in range(len(wegame_c))]

    #merge the external and WeGame datasets
    dataset = pd.concat([outgames_c, wegame_c])
    #print(dataset.info())

    #make soup
    # Add soup a column
    dataset['soup'] = dataset.apply(make_soup, axis=1)

    #return new dataset
    return dataset


def get_games_user_likes(games, user_data_file):
    game_names = []
    with open(f"{os.getcwd()}{user_data_file}") as f:
        user = json.load(f)
    
    for game_name in user[0].keys():
        r = find_game_info_in_db(game_name, games)
        if r is not None:
            game_names.append(r)
        #game_obj = Game(game_row["name"], game_row["themes"], game_row["genres"], game_row["game_modes"], game_row["povs"])
    return game_names


def get_reccommendations(data, name):
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(data['soup'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    
    data = data.reset_index()
    indices = pd.Series(data.index, index=data['name']).drop_duplicates()
    #print(indices[:10])
    
    # Get the index of the game that matches the name
    idx = indices[name]

    # Get the pairwsie similarity scores of all games with that game
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the games based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the game indices for top matches on our platform.
    best_matches = []
    game_indices = [i[0] for i in sim_scores]
    for index in game_indices:
        if data.iloc[index]["WeGame"] == True:
            best_matches.append(data.iloc[index]["name"])

    return best_matches


"""The series of reccomendations in the order to be displayed to user.
It is an array of Series"""
final_reccs = []
games = preprocess_data(GAME_DATA_PATH, WEGAME_GAMES_DATA_PATH)
#wegame_data = deepcopy(games[games["WeGame"] == True])
#external_data = deepcopy(games[games["WeGame"] == False])

for game in get_games_user_likes(games, USER_DATA_PATH):
    reccs = get_reccommendations(games, game["name"])
    for i, recc in enumerate(reccs):
        if recc not in final_reccs:
            final_reccs.append(recc)
            break

print("Your current reccomendation(s) based on your steam account and our current data")
print(final_reccs)