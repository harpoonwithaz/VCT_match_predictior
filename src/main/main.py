# VCT match outcome prediction algorithm

# Imports requests, json, and pandas module (Needs to be installed through pip3)
import requests
import json
import pandas as pd

# Function to check if request is valid and returns json data
def get_json_data(response):
    # Check if the request was successful
    if response.status_code == 200:
        json_data = response.json()
    else:
        print('Failed to retrieve data from the API')
        json_data = None
    # Returns json data
    return json_data

def get_team_id(team_name):
    a = 'a'

# Basic team data of all VCT teams
all_teams = requests.get('https://vlr.orlandomm.net/api/v1/teams?limit=4')

# Gets json data and converts to pandas dataframe
json_data = pd.DataFrame(get_json_data(all_teams)['data'])

print(json_data['name'][0]) 