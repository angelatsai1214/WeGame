# Take in the user's list of games, in the order of their prefrence, from SteamUser file
# For each of these games, compute the most similar game(s) to it, and add to a list
# If the reccomendation is duplicate, choose the next one, until none are left. In that case 
# skip it

# For now, since there arent alot of games on the platform, only reccomend one game per 
# each game in the library, later change this to be dependatn on user settings

#How to make recommendations?
#Our platform and igdb have the same criteria, so it will be like reccomending from 
#the same dataset
import json
import pandas as pd
from typing import List, Dict
from copy import deepcopy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#class Game():
#    """An object representing a game in the database.
#    Must have a name, theme, genre, game mode, and player perspective"""
#    def __init__(self, name:str, themes:List, genres:List, game_modes:List, povs:List):
#        self.name = name
#        self.themes = themes
#        self.genres = genres
#        self.game_modes = game_modes
#        self.povs = povs


USER_DATA_PATH = "\dataClean\SampleSteamUser.json"
WEGAME_GAMES_DATA_PATH = "\dataClean\SampleWeGameDevs"
OUTPUT_RECCOMMENDATIOS_FILE = "\dataClean\SampleReccs.json"
GAME_DATA_PATH = "\dataClean\games01.json"
LIMIT = 20

def save_data(reccs:Dict):
    with open(OUTPUT_RECCOMMENDATIOS_FILE, "w") as file:
        json.dump(reccs, file)


def find_game_info_in_db(game_name:str, db:pd.DataFrame)->pd.Series:
    result = db.index[db["name"] == game_name].tolist()
    if len(result) == 1:
        return result.iloc[result[0]]
    elif len(result) > 1:
        raise Exception(f"There is a conflict for the values of the game {game_name}, there are two games with the same name")


def make_soup(x):
    genres = ' '.join(x["genres"])
    game_modes = ' '.join(x["game_modes"])
    themes = ' '.join(x["themes"])
    player_perspectives = ' '.join(x["player_perspectives"])
    return ' '.join(x["name"], genres, game_modes, themes, player_perspectives)


def preprocess_data(external_games_data_file, internal_games_data_file):
    """Process data and make it ready for use
    @games_data_file: The file path for the file that stores all the data on
    the video games from external sources like steam or playstation store.
    Has many data fields and is fetched from igdb's API, using igdb.py
    @user_data_file: The file path for the file that stores all the data on users gaming
    history. Currently only Steam."""
    outgames = pd.read_json(external_games_data_file)
    wegame = pd.read_json(internal_games_data_file)
    
    #Deepcopy the subset of dfs that are important and continue working with those
    fields = ["name", "game_modes", "player_perspectives", "genres", "themes"]
    outgames_c = deepcopy(outgames[fields])
    wegame_c = deepcopy(wegame[fields])
    
    #Add a weGame column for confirming the source
    outgames_c["WeGame"] = [True for _ in range(len(outgames_c))]
    wegame_c["WeGame"] = [True for _ in range(len(wegame_c))]

    #merge the external and WeGame datasets
    dataset = outgames_c.concat(wegame_c)

    #make soup
    # Add soup a column
    dataset["soup"] = dataset.apply(make_soup)
    
    #return new dataset
    return dataset


def get_games_user_likes(games, user_data_file):
    game_objs = []
    with open(user_data_file) as f:
        user = json.load(f)
    
    for game_name in user[0].keys():
        game_objs.append(find_game_info_in_db(game_name, games))
        #game_obj = Game(game_row["name"], game_row["themes"], game_row["genres"], game_row["game_modes"], game_row["povs"])
    return game_objs



def get_reccommendations(data, name):
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(data['soup'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    
    indices = pd.Series(data.index, index=data['name']).drop_duplicates()
    print(indices[:10])
    
    # Get the index of the game that matches the name
    idx = indices[name]

    # Get the pairwsie similarity scores of all games with that game
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the games based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the game indices for top games on our platform.
    best_matches = []
    game_indices = [i[0] for i in sim_scores]
    for index in game_indices:
        if data.iloc[index]["WeGame"]:
            best_matches.append(data.iloc[index]["name"])

    if len(best_matches) <= 20:
        return best_matches
    else:
        return best_matches[:20]


"""The series of reccomendations in the order to be displayed to user.
It is an array of Series"""
final_reccs = []
games = preprocess_data(GAME_DATA_PATH, WEGAME_GAMES_DATA_PATH)
for game in get_games_user_likes(games, USER_DATA_PATH):
    reccs = get_reccommendations(games, game["name"])
    for i, recc in enumerate(reccs):
        if recc not in final_reccs:
            final_reccs.append(recc)
            break

print(final_reccs)