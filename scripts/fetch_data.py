import requests
import logging
from config import API_KEY

BASE_URL = "https://api.nasa.gov/neo/rest/v1/neo/browse"
#BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08"

def fetch_all_neo_data():
    logger = logging.getLogger()
    url = f"{BASE_URL}?api_key={API_KEY}"
    all_data = []  # List to store all results

   # while url:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        all_data.extend(data['near_earth_objects'])  # Append the current page's data
        url = data.get('links', {}).get('next')  # Move to the next page if available
        logger.info(f"Fetched page: {BASE_URL}")
    except requests.RequestException as e:
        logger.error(f"Error fetching data from NASA API: {e}")
    #break
    return all_data
