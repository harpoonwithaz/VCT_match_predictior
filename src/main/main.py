# VCT match outcome prediction algorithm

# Imports requests, json, and pandas module (Needs to be installed through pip3)
import pandas as pd
import file_paths
from api_modules import obtain_api_data

#match_results_df = obtain_api_data.fetch_match_results()
#match_results_df.to_csv(file_paths.api_match_results, index=False)

#all_teams = obtain_api_data.fetch_all_teams(['na'])
#print(all_teams)

# 2593 | Test team ID (Fnatic)
#team_data = obtain_api_data.fetch_team(2593)
#print(team_data)


all_players = obtain_api_data.fetch_all_players(country = 'ca', agent = 'omen', result_limit = "all")
print(all_players)

# Test ID: 9 (TenZ)
#player_data = obtain_api_data.fetch_player(9)
#print(player_data)