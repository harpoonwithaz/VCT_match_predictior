# VCT match outcome prediction algorithm

# Imports requests, json, and pandas module (Needs to be installed through pip3)
import requests
import json
import os
import pandas as pd
import file_paths
from api_modules.obtain_match_results import fetch_match_results

match_results_df = fetch_match_results()
match_results_df.to_csv(file_paths.api_match_results, index=False)
