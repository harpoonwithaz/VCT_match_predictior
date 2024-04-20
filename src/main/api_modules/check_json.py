# Function to check if request is valid and returns json data
def get_json_data(response):
    """
    Extracts JSON data from the response if the request was successful.

    Args:
    response: The response object from the API request.

    Returns:
    JSON data if the request was successful, otherwise None.
    """
    # Check if the request was successful
    if response.status_code == 200:
        json_data = response.json()
    else:
        print('Failed to retrieve data from the API')
        json_data = None
    # Returns json data
    return json_data