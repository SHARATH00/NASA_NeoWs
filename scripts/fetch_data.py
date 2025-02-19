import requests
import logging
from config import API_KEY

BASE_URL = "https://api.nasa.gov/neo/rest/v1/neo/browse"
#BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08"

def fetch_all_neo_data():
    logger = logging.getLogger()
    url = f"{BASE_URL}?api_key={API_KEY}"
    all_data = []  # List to store all results
    page_count = 0  # Counter to keep track of the number of pages fetched

    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()

            # Check if near_earth_objects is not empty
            if not data.get('near_earth_objects'):
                logger.info("No more near earth objects to fetch.")
                break
            
            all_data.extend(data['near_earth_objects'])  # Append the current page's data
            url = data.get('links', {}).get('next')  # Move to the next page if available
            # Log the current URL without the API key
            log_url = url.split('&api_key=')[0]
            logger.info(f"Fetched page: {log_url}")
            #logger.info(f"Fetched page: {BASE_URL}")

            # Increment the page count
            page_count += 1
            logger.info(f"Page count: {page_count}")
            # Break the loop if 500 pages have been fetched
            #if page_count >= 100:
            #logger.info("Fetched 500 pages, stopping further requests.")
               # break

        except requests.RequestException as e:
            logger.error(f"Error fetching data from NASA API: {e}")
            break
    return all_data
