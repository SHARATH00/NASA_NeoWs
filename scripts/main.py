from fetch_data import fetch_all_neo_data
from database import connect_db, upsert_data
from data_checks import validate_api_response
from logger import logger

def main():
    try:
        # Fetch data
        data = fetch_all_neo_data()
        # validate_api_response(data)

        # Process data
        asteroids = []
        close_approaches = []
        for obj in data:
            # Process asteroid data
            asteroid = (
                obj['id'], obj['name'], obj['neo_reference_id'], obj['absolute_magnitude_h'],
                obj['estimated_diameter']['kilometers']['estimated_diameter_min'],
                obj['estimated_diameter']['kilometers']['estimated_diameter_max'],
                (obj['estimated_diameter']['kilometers']['estimated_diameter_min'] + obj['estimated_diameter']['kilometers']['estimated_diameter_max']) / 2,
                obj['is_potentially_hazardous_asteroid'], obj['orbital_data']['orbit_id'],
                obj['orbital_data']['orbit_determination_date'], obj['orbital_data']['first_observation_date'],
                obj['orbital_data']['last_observation_date'], obj['orbital_data']['data_arc_in_days'],
                obj['orbital_data']['observations_used'], obj['orbital_data']['orbit_uncertainty'],
                obj['orbital_data']['minimum_orbit_intersection'], obj['orbital_data']['jupiter_tisserand_invariant'],
                obj['orbital_data']['epoch_osculation'], obj['orbital_data']['eccentricity'],
                obj['orbital_data']['semi_major_axis'], obj['orbital_data']['inclination'],
                obj['orbital_data']['ascending_node_longitude'], obj['orbital_data']['orbital_period'],
                obj['orbital_data']['perihelion_distance'], obj['orbital_data']['perihelion_argument'],
                obj['orbital_data']['aphelion_distance'], obj['orbital_data']['perihelion_time'],
                obj['orbital_data']['mean_anomaly'], obj['orbital_data']['mean_motion'],
                obj['orbital_data']['equinox'], obj['orbital_data']['orbit_class']['orbit_class_type'],
                obj['orbital_data']['orbit_class']['orbit_class_description'], obj['orbital_data']['orbit_class']['orbit_class_range'],
                obj['is_sentry_object']
            )
            asteroids.append(asteroid)

            # Process close approach data
            for approach in obj['close_approach_data']:
                close_approach = (
                    obj['id'], approach['close_approach_date'], approach['close_approach_date_full'],
                    approach['epoch_date_close_approach'], approach['relative_velocity']['kilometers_per_second'],
                    approach['relative_velocity']['kilometers_per_hour'], approach['relative_velocity']['miles_per_hour'],
                    approach['miss_distance']['astronomical'], approach['miss_distance']['lunar'],
                    approach['miss_distance']['kilometers'], approach['miss_distance']['miles'],
                    approach['orbiting_body']
                )
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