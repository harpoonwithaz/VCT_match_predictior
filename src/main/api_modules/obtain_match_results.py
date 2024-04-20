import requests
import pandas as pd
import file_paths
from api_modules import check_json

# Function to fetch match results from api, and return results as dataframe
def fetch_match_results():
    """
    Fetches match results from API and returns them as a dataframe.

    Returns:
    A dataframe containing match results.
    """
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
    for page_number in range(10):
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
    print(records_amount, 'new records added')

    # Sets insert index to first row of dataframe
    insert_index = 0

    # Split df into two parts and concatenate api data in between
    df = pd.concat([df.iloc[:insert_index], api_data, df.iloc[insert_index:]], ignore_index=True)
    return df