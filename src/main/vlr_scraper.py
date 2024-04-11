from bs4 import BeautifulSoup
import requests

# Function to take match data from vlr and return it as list
def get_match_data(match_id):
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
    
    # Gets top header from vlr match result page
    match_header_vs = soup.find('div', class_ = 'match-header-vs')

    # Gets 2 team names html, strips html tags and assigns each team name as to a list
    team_name_html = match_header_vs.find_all('div', class_ = 'wf-title-med')
    team_names = [names.text.strip() for names in team_name_html]

    # Gets score html, 
    match_score_html = match_header_vs.find('div', class_ = 'js-spoiler')
    match_score = match_score_html.find_all('span')


    team_vetoes = match_header_vs
    print(team_names)
    print(match_score)
    
    """
    stats_container = soup.find('div', class_ = 'vm-stats-container')
    print(soup)
    """

# Test match id: 318919 (Team Vitality Vs Team Heretics, Wednesday, April 10th, 11:10 AM PDT)
        
get_match_data(318919)