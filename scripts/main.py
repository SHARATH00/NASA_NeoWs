# main.py
from fetch_data import fetch_neo_data
from database import connect_db, upsert_data
from data_checks import validate_api_response
from logger import logger

def main():
    try:
        # Fetch data
        data = fetch_neo_data()
        validate_api_response(data)

        # Process data
        asteroids = []
        close_approaches = []
        for objects in data['near_earth_objects'].values():
            for obj in objects:
                # Process asteroid data (example logic)
                asteroid = (
                    obj['id'], obj['name'], obj['neo_reference_id'], obj['absolute_magnitude_h']
                )
                asteroids.append(asteroid)

                # Process close approach data
                for approach in obj['close_approach_data']:
                    close_approach = (obj['id'], approach['close_approach_date'])
                    close_approaches.append(close_approach)

        # Save to database
        conn = connect_db()
        upsert_data(conn, asteroids, close_approaches)
        conn.close()
        logger.info("Pipeline completed successfully.")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
