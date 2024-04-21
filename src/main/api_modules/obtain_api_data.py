import requests
import pandas as pd
import time
import file_paths
from api_modules import check_json

# Function to get match results from api, and return results as dataframe
def fetch_match_results():
    """
    Fetches match results from API and returns them as a dataframe.

    Returns:
    A dataframe containing match results.
    """
    start_time = time.time()  # Record the start time
    
    # Defines amount of records
    records_amount = 0

    # Defines dataframe column names
    df_columns = ['id', 'teams', 'status', 'ago', 'event', 'tournament', 'img']

    # Assigns all new API data
    api_data = pd.DataFrame(columns = df_columns)

    # Try to read CSV data into a dataframe; create a new file if not found
    try:
        df = pd.read_csv(file_paths.api_match_results)
    except FileNotFoundError:
        print('File not found error, creating new file')
        df = pd.DataFrame(columns = df_columns)
        df.to_csv(file_paths.api_match_results, index = False)

    # Initialize flag variable
    break_out = False

    ## Iterates over a set number of API pages
    for page_number in range(10):  # This number is just a temporary test number to get the last 4 pages of the api
        print('Reading page:', page_number + 493)

        # Makes request to get all results from specified API page
        all_results = requests.get(f'https://vlr.orlandomm.net/api/v1/results?page={page_number + 493}')

        # Gets json data
        json_data = check_json.get_json_data(all_results)

        # Checks if there is no data, breaks for loop
        if json_data['size'] == 0:
            print('There is no data remaining')
            break_out = True  # Set flag to break both loops
            break
        else:
            # Converts json data to dataframe
            match_data = pd.DataFrame(json_data['data'])

            # Repeats the amount of times of data on page
            for row_index in range(len(match_data)):
                # Checks for duplicates in match ids in the dataframe to the csv file
                if int(match_data['id'][row_index]) in df['id'].tolist():
                    print('Duplicate found')
                    break_out = True  # Set flag to break both loops
                    break
                else:
                    records_amount += 1
                    # Appends current row to api dataframe
                    api_data = api_data._append(match_data.loc[row_index])
            
            if break_out:
                break  # Break outer loop
    
    # Prints amount of new records
    print(records_amount, 'new matches found')

    # Sets insert index to first row of dataframe
    insert_index = 0

    # Split df into two parts and concatenate api data in between
    df = pd.concat([df.iloc[:insert_index], api_data, df.iloc[insert_index:]], ignore_index=True)
        
    # Record the end time, calculates execution time and prints it
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    return df

# Function to get all VCT teams basic info from api, and return them as dataframe
def fetch_all_teams(region: str):
    """
    Fetches all VCT teams basic info from API and returns them as a dataframe.

    Returns:
    A dataframe containing all VCT teams basic info.
    """
    start_time = time.time()  # Record the start time
    
    # Defines dataframe column names
    df_columns = ['id', 'url', 'name', 'img', 'country']

    # Creates new data frame for all teams
    df = pd.DataFrame(columns = df_columns)

    # Makes a request to the API
    all_teams = requests.get(f'https://vlr.orlandomm.net/api/v1/teams?limit=all')
    
    # Gets json data
    json_data = check_json.get_json_data(all_teams)

    # Appends json data to df and returns it
    df = df._append(json_data['data'])
        
    # Record the end time, calculates execution time and prints it
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    return df

# Function to get specific team data using team ids from api, and returns them as dataframe
def fetch_team(team_id: int):
    """
    Fetches detailed info of specific team from API and returns them as a dataframe. Requires teams unique ID.

    Parameters:
    team_id (int): Specific teams unique ID.
        This parameter represents the teams unique ID to pass to the URL to make a call to the api containing the teams specific data.

    Returns:
    A dataframe containing detailed info of specific team.
    """
    start_time = time.time()  # Record the start time
    
    # Defines dataframe column names
    df_columns = ['players', 'staff', 'events', 'results', 'upcoming']

    # Creates new data frame for all teams
    df = pd.DataFrame(columns = df_columns)

    # Makes a request to the API
    team_data = requests.get(f'https://vlr.orlandomm.net/api/v1/teams/{team_id}')

    # Gets json data
    json_data = check_json.get_json_data(team_data)

    # Appends json data to df and returns it
    df = df._append(json_data['data'], ignore_index=True)
    
    # Record the end time, calculates execution time and prints it
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    return df

# Function to get all players data from api, and returns them as dataframe
def fetch_all_players():
    """
    Fetches all players data from api, and returns them as dataframe.

    Returns:
    A dataframe containing all players data.
    """
    start_time = time.time()  # Record the start time
    
    # Defines dataframe column names
    df_columns = ['id', 'url', 'name', 'teamTag', 'country']

    # Creates new data frame for all teams
    df = pd.DataFrame(columns = df_columns)

    # Makes a request to the API
    all_players = requests.get('https://vlr.orlandomm.net/api/v1/players?limit=all')

    # Gets json data
    json_data = check_json.get_json_data(all_players)

    # Appends json data to df
    df = df._append(json_data['data'])

    # Record the end time, calculates execution time and prints it
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    # Returns json data
    return df

def fetch_player(player_id: int):
    """
    Fetches detailed info of specific player from API and returns them as a dataframe. Requires players unique ID.

    Parameters:
    player_id (int): Specific players unique ID.
        This parameter represents the players unique ID to pass to the URL to make a call to the api containing the players specific data.

    Returns:
    A dataframe containing detailed info of specific player.
    """
    start_time = time.time()  # Record the start time
    
    # Defines dataframe column names
    df_columns = ['info', 'string', 'team', 'pastTeams', 'socials']

    # Creates new data frame for all teams
    df = pd.DataFrame(columns = df_columns)

    # Makes a request to the API
    player_data = requests.get(f'https://vlr.orlandomm.net/api/v1/teams/{player_id}')

    # Gets json data
    json_data = check_json.get_json_data(player_data)

    # Appends json data to df and returns it
    df = df._append(json_data['data'])
    
    # Record the end time, calculates execution time and prints it
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    return df