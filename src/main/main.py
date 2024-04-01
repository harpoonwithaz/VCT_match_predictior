# VCT match outcome prediction algorithm

import requests
import json
import pandas as pd

# Basic team data of all VCT teams
all_teams = requests.get("https://vlr.orlandomm.net/api/v1/teams?region=all")

def get_json_data(response):
    # Check if the request was successful
    if response.status_code == 200:
        json_data = response.json()
    else:
        print("Failed to retrieve data from the API")
        json_data = None
    # Returns json data
    return json_data

test = get_json_data(all_teams)
print(type(test))