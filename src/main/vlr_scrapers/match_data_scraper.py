from bs4 import BeautifulSoup
import requests

# Function to take match data from vlr and return it as list, and returns the processed match id
def get_match_data(match_id):
    processed_match_id = match_id
    # Send a request to the specified URL
    url = f'https://www.vlr.gg/{match_id}'
    page = requests.get(url)

    # Checks if request was successful
    if page.status_code == 200:
        # Gets HTML of URL
        soup = BeautifulSoup(page.text, 'html.parser')
    else:
        print('Failed to retrieve data')

    # =================
    # TEAM RELATED DATA
    # =================

    # Extracts team names
    team_name_html = soup.find_all('div', class_ = 'wf-title-med')
    team_names = [names.text.strip() for names in team_name_html]

    # Extracts match score
    match_score_html = (soup.find('div', class_ = 'js-spoiler')).find_all('span')
    match_score = [score.text.strip() for score in match_score_html]
    match_score.remove(':')

    # Extracts maps played

    team_vetoes = soup
    print(team_names)
    print(match_score)
    
    """
    stats_container = soup.find('div', class_ = 'vm-stats-container')
    print(soup)
    """

# Test match id: 318919 (VIT VS TH, Wednesday, April 10th, 11:10 AM PDT)
# 314625 (SEN VS 100T)
        
get_match_data(318919)