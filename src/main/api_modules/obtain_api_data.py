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
def fetch_all_teams(region: str = "all"):
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
    all_teams = requests.get(f'https://vlr.orlandomm.net/api/v1/teams?limit=all&region={region}')
    
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
def fetch_all_players(result_limit = None,
                    event_series_id : int = None, 
                    specific_event_id : int = None, 
                    #region : str = None, 
                    country : str = None, 
                    min_rounds : int = 0, 
                    min_rating : int = 0,
                    agent : str = None,
                    map_id : int = None,
                    time_span : str = None):  # Parameters for the URL, they are not required to be given args when calling the function
    """
    Fetches all players teams basic info from API and returns them as a dataframe.

    Parameters (Args not required):
    result_limit (int/str): Limit of results per page. You can also use all to get all players. If no args given, sets to 10 results.
        This parameter represents the limit of results per page (Ex. all, 10, 15, 34, etc.) which is passed to the URL to make a call to the api containing the data with that parameter.

    event_series_id (int): Specific ID of event series. If no args given, sets to all events.
        This parameter represents the event series (Ex. Valorant Champions Tour 2024, Valorant Game Changers 2024, etc.) unique ID which is passed to the URL to make a call to the api containing the data with that parameter.

    specific_event_id (int): Specific ID of specific event in the event series. If no args given, sets to all event series.
        This parameter represents the specific event in the event series (Ex. Champions Tour 2024: Americas Kickoff, Champions Tour 2024: Masters Madrid, etc.) unique ID which is passed to the URL to make a call to the api containing the data with that parameter.

    region (str): 2/3 letter abbreviation for players region. If no args given, sets to all regions. CURRENTLY NOT WORKING
        This parameter represents the 2/3 letter abbreviation for players region (Ex. na, eu, oce, etc.) which is passed to the URL to make a call to the api containing the data with that parameter.

    country (str): 2/3 letter abbreviation for players country. If no args given, sets to all countries.
        This parameter represents the 2/3 letter abbreviation for players country (Ex. ca, us, etc.) which is passed to the URL to make a call to the api containing the data with that parameter.

    min_rounds (int): Minimum rounds player played. By default is set to 0.
        This parameter represents the minimum rounds a player has played which is passed to the URL to make a call to the api containing the data with that parameter.

    min_rating (int): Minimum rating of player. By default is set to 0.
        This parameter represents the minimum rating a player has which is passed to the URL to make a call to the api containing the data with that parameter.

    agent (str): Specific agent. If no args given, sets to all agents.
        This parameter represents one agent (Ex. jett, astra, etc.) a player has played which is passed to the URL to make a call to the api containing the data with that parameter.

    map_id (int): Specific id of certain map. If no args given, sets to all maps.
        This parameter represents the stats of a certain player on a certain map (Ex. split, bind, etc.) unique ID which is passed to the URL to make a call to the api containing the data with that parameter.

    time_span (str): Time period. If no args given, sets to 60d.
        This parameter represents the time period of players stats (Ex. all, 30d, 60d, etc.) which is passed to the URL to make a call to the api containing the data with that parameter.

    Returns:
    A dataframe containing all players data with specific parameter.
    """
    start_time = time.time()  # Record the start time
    
    # Defines dataframe column names
    df_columns = ['id', 'url', 'name', 'teamTag', 'country']

    # Creates new data frame for all teams
    df = pd.DataFrame(columns = df_columns)

    # Constructing the URL parameters dynamically
    url_args = ""
    params = [
        ('limit', result_limit),
        ('event_series_id', event_series_id),
        ('specific_event_id', specific_event_id),
        #('region', region),
        ('country', country),
        ('min_rounds', min_rounds),
        ('min_rating', min_rating),
        ('agent', agent),
        ('map_id', map_id),
        ('time_span', time_span)
    ]
    
    # Add parameters to url_args if they are not None
    for param_name, param_value in params:
        if param_value is not None:
            url_args += f"{param_name}={param_value}&"

    # Remove the last '&' if url_args is not empty
    if url_args:
        url_args = '?' + url_args[:-1]

    print(url_args)

    # Makes a request to the API with the api url args
    all_players = requests.get(f'https://vlr.orlandomm.net/api/v1/players{url_args}')

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

# Function to get detailed player info on specified player from api and return it as a dataframe
def fetch_player(player_id: int):
    """
    Fetches detailed info of specific player from API and returns them as a dataframe. Requires players unique ID.

    Parameters:
    player_id (int): Specific players unique ID.
        This parameter represents the players unique ID which is passed to the URL to make a call to the api containing the players specific data.

    Returns:
    A dataframe containing detailed info of specific player.
    """
    start_time = time.time()  # Record the start time
    
    # Defines dataframe column names
    df_columns = ['info', 'team', 'results', 'pastTeams', 'socials']

    # Creates new data frame for all teams
    df = pd.DataFrame(columns = df_columns)

    # Makes a request to the API
    player_data = requests.get(f'https://vlr.orlandomm.net/api/v1/players/{player_id}')

    # Gets json data
    json_data = check_json.get_json_data(player_data)

    # Appends json data to df and returns it
    df = df._append(json_data['data'], ignore_index = True)
    
    # Record the end time, calculates execution time and prints it
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    return df

# Function to get details on events from api and return is as a dataframe
def fetch_all_events(event_status : str = None, event_region : str = None):
    """
    Fetches details about valorant events from API and returns them as a dataframe.

    Parameters:
    event_status (int): Filters events by their status. 
        This parameter represents the events status (ongoing, upcoming, completed, all) which is passed to the URL to make a call to the api containing the players specific data.

    Returns:
    A dataframe containing details on valorant events.
    """
    start_time = time.time()  # Record the start time
    
    # Defines dataframe column names
    df_columns = ['id', 'name', 'status', 'prizepool', 'dates', 'country', 'img']

    # Creates new data frame for all teams
    df = pd.DataFrame(columns = df_columns)

    # Constructing the URL parameters dynamically
    url_args = ""
    params = [
        ('status', event_status),
        ('region', event_region),
    ]
    
    # Add parameters to url_args if they are not None
    for param_name, param_value in params:
        if param_value is not None:
            url_args += f"{param_name}={param_value}&"

    # Remove the last '&' if url_args is not empty
    if url_args:
        url_args = '?' + url_args[:-1]

    # Makes a request to the API with the api url args
    events = requests.get(f'https://vlr.orlandomm.net/api/v1/players?{url_args}')

    # Gets json data
    json_data = check_json.get_json_data(events)

    # Appends json data to df
    df = df._append(json_data['data'])

    # Record the end time, calculates execution time and prints it
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    # Returns json data
    return df