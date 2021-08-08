"""This file is the command prompt app for downloading all the data from a specific endpoint
from the igdb api. This data is downloaded as files in order to be usef t=for the recommendation engine
It was used only to get data, and will not be used in production"""

import json
import requests
import argparse



parser = argparse.ArgumentParser(description='Get all the entries for a given endpoint for the igdb API')

parser.add_argument('endpoint', help='The endpoint to query. A ')

parser.add_argument('client_id', help='The Client-ID aquired from the twitch developer website after registering an application.\
More information can be found here: https://api-docs.igdb.com/#account-creation')

parser.add_argument('access_token', help='The access token is given after making a post requests to https://id.twitch.tv/oauth2/token\
with the query parameters as client id, access token and credentials. example using curl:\
curl -X POST "https://id.twitch.tv/oauth2/token?client_id=5ssedltnurqii57m86x43jq7j8m0go&client_secret=270sfxcmbd4oe96a5nobgragp7ghg8&grant_type=client_credentials"\
More information can be found at https://api-docs.igdb.com/#authentication')

parser.add_argument('-o', '--output', help='The value will be stored at the json file specified by the user. If no value is passed in, results will be printed')

parser.add_argument('-s', '--seperate_files', action='store_true', help='If specified, the result of each request(where each reault)\
has the result of 500 entries max) will be stored in seperate files.')

parser.add_argument('-v', '--verbose', action='store_true', help='Specify to get an ouput specifying the number of entries after\
each request.')

args = parser.parse_args()

#Used by program, not set by user in interface
BASE_URL = "https://api.igdb.com/v4/"
HEADERS = {'Client-ID': args.client_id, 'Authorization': f'Bearer {args.access_token}', 'Accept': 'application/json'}
LIMIT = 500  #THE API has a limit of 500 per request
offset = -LIMIT #Set to 500 so that in the first iteration it becomes 0
has_more_entries = True
file_num = 0
row_num = 0

while has_more_entries:
    offset += LIMIT
    
    if args.output != None and args.seperate_files:
        file_num += 1
    
    response = requests.post(f'{BASE_URL}{args.endpoint}', data=f'fields *; limit {LIMIT}; offset {offset};', headers=HEADERS)
    json_obj = response.json()
    curr_row_num = len(json_obj)
    row_num += curr_row_num
    
    if curr_row_num < LIMIT:
        has_more_entries = False
    
    if args.output != None:
        if args.seperate_files:
            file_name = f'{args.output}{file_num}.json'
        else:
            file_name = f'{args.output}.json'

        with open(file_name, 'a') as f:
            json.dump(json_obj, f)
    else:
        print(response.json())

    if args.verbose:
        print("Number of rows for this request:", curr_row_num)
        print("Total number of rows: ", row_num)

print(f"There were {row_num} rows in total.")