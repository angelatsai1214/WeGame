from numpy import positive
from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import argparse
import json
import pandas as pd
import re
from typing import Dict, Tuple, Union
from requests.models import HTTPError
import numpy as np



#TODO: Also fetch reviews and add them as a parameter for sorting each entry later
"""Get data for a users games from steam. This file would get executed once
when the user links their account, and fetched their data, then sorts it based on users
playing time and other factors so that other files can use it"""

def clear(string):
    """return: Returns the string, stripped of all letters except alphanum
    If the string doesnt contain alphanum or only conatins numbers, None is returned"""
    string = re.sub("[^A-Za-z0-9]+", "", string)
    if (string.isdecimal()) or (len(string) == 0):
        return None
    return string

def min_to_hrs(min)->float:
    return min / 60


def get_games(api_key:str, steam_id:str, clear:Union[None, function], to_hrs=True) -> Dict[]:
    """API key from https://steamcommunity.com/dev/apikey
    and steamid available for each logged in account here https://store.steampowered.com/account/"""
    #TODO: add async to make faster requests for users with lots of games
    games = {}
    URL = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=\
{api_key}&steamid={steam_id}&format=json"
    BASE_URL_APPID = "https://store.steampowered.com/app/"
    r = requests.get(URL)
    if r.status_code == 200:
        user_obj = r.json()
        for item in user_obj["response"]["games"]:
            print(BASE_URL_APPID+str(item["appid"]))
            game_name_r = requests.get(BASE_URL_APPID+str(item["appid"]))
            game_name_soup = BeautifulSoup(game_name_r.text, "html5lib")
            game_name = game_name_soup.find("div", id="appHubAppName").text.strip()
            if clear != None:
                game_name = clear(game_name)
            if not to_hrs:
                games[game_name] = item["playtime_forever"]
            else:
                games[game_name] = min_to_hrs(item["playtime_forever"])
        return games
    #remove in production
    elif r.status_code == 401:
        raise HTTPError("Invalid key")
    elif r.status_code == 500:
        raise HTTPError("username doesnt exist. Double check username or set account to public.")
    else:
        raise HTTPError("Error Loading, try again later")


def calculateAvgTimeFromDF(avg_time_df:DataFrame) -> Dict[str, float]:
    """returns: Average of all avaliable times that arent Nan"""
    avg_time_dict = {}
    times = [col for col in avg_time_df.columns if "time" in col]
    for i, row in avg_time_df.iterrows():
        curr_row_times = []
        for time_col in times:
            if not np.notna(row[time_col]):
                curr_row_times.append(row[time_col])
        avg = sum(curr_row_times) / len(curr_row_times)
        avg_time_dict[row["name"]] = avg
    return avg_time_dict


def sort_based_on_activity(avg_time_file:str, games_activity: Dict[str, int]) -> Dict[Tuple[str, float], float]:
    """
    @avgTimeFile: The CSV or JSON file that contains the data for the average time of each video game
    File has columns that includes playing time based on Main Story time, Main + Extra time,
    Completionist time, Solo time, Co-op time, Vs.time. It also includes info about an estimate of
    number of people who have voted for the times. 
    @gamesActivity: The dictionary mapping the name of the game to the amount of time user spent playing it
    return: Returns the gamesActivity dictionary in order
    """
    #Initialize dict with by using the game name and time as keys
    games_priority = {}
    for game_name, user_time in games_activity.items():
        games_priority[(game_name, user_time)] = 0.0

    #set the value to the tme difference between users playtime and the average playtime
    if avg_time_file[avg_time_file.find("."):] == "json":
        avg_time_df = pd.read_json(avg_time_file)
    elif avg_time_file[avg_time_file.find("."):] == "csv":
        avg_time_df = pd.read_csv(avg_time_file)
    else:
        raise FileNotFoundError("The extension has to be json or csv");
    
    avg_time_dict = calculateAvgTimeFromDF(avg_time_df)
    for game_name, user_time in games_activity.items():
        try:
            avg_time = avg_time_dict[game_name]
            time_diff = float(user_time) - float(avg_time)
            games_priority[(game_name, user_time)] = time_diff
        except:
            #If no data is available, assume completly average time
            games_priority[(game_name, user_time)] = 0

    #sort all positives values first, big to small, and then negative values
    #small to big
    positives_sorted = []
    negatives_sorted = []
    for obj, diff in games_priority.items():
        if diff >= 0:
            positives_sorted.append((obj, diff))
        else:
            negatives_sorted.append((obj, diff))
    
    positives_sorted = sorted(positives_sorted, key=lambda item: item[1], reverse=True)
    negatives_sorted = sorted(negatives_sorted, key=lambda item: item[1])

    return dict(positives_sorted + negatives_sorted)


def save_games(games_dict: dict, outfile:str):
    """
    input: Takes in a dictionary containging mappingnthe name of the game to th
    Saves the data to a json file with the name of outfile
    """
    with open(outfile, 'w') as file:
        json.dump(games_dict, file)
    

parser = argparse.ArgumentParser(description="Command line interface for getting data for user")
parser.add_argument("steamId", help="Make sure your profile is set as public. Then sign in to your account\
and go to https://store.steampowered.com/account/ where you will see your steam ID below the username")
parser.add_argument("APIKey", help="https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerAchievements_.28v0002.29 is the docs\
for the API. Get API key from https://steamcommunity.com/dev/apikey")
args = parser.parse_args()

user_games = get_games(str(args.APIKey), str(args.steamId))
save_games(sort_based_on_activity("./dataClean/timeclean.csv", user_games), "SampleSteamUser.json")
