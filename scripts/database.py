import pg8000
from config import DB_CONFIG
from logger import logger

def connect_db():
    """
    Establish a connection to the PostgreSQL database using pg8000.
    """
    try:
        conn = pg8000.connect(
            database=DB_CONFIG['dbname'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
        logger.info("Database connection established.")
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise

def upsert_data(conn, asteroid_data, close_approach_data):
    """
    Inserts or updates asteroid and close approach data using pg8000.
    """
    with conn.cursor() as cur:
        # Insert Asteroid Data
        asteroid_query = '''
        INSERT INTO neo_data.asteroids (id, name, neo_reference_id, absolute_magnitude_h, estimated_diameter_min_km,
        estimated_diameter_max_km, estimated_diameter_mean_km, is_potentially_hazardous_asteroid, orbit_id,
        orbit_determination_date, first_observation_date, last_observation_date, data_arc_in_days, observations_used,
        orbit_uncertainty, minimum_orbit_intersection, jupiter_tisserand_invariant, epoch_osculation, eccentricity,
        semi_major_axis, inclination, ascending_node_longitude, orbital_period, perihelion_distance, perihelion_argument,
        aphelion_distance, perihelion_time, mean_anomaly, mean_motion, equinox, orbit_class_type, orbit_class_description,
        orbit_class_range, is_sentry_object)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
        name = EXCLUDED.name,
        neo_reference_id = EXCLUDED.neo_reference_id,
        absolute_magnitude_h = EXCLUDED.absolute_magnitude_h,
        estimated_diameter_min_km = EXCLUDED.estimated_diameter_min_km,
        estimated_diameter_max_km = EXCLUDED.estimated_diameter_max_km,
        estimated_diameter_mean_km = EXCLUDED.estimated_diameter_mean_km,
        is_potentially_hazardous_asteroid = EXCLUDED.is_potentially_hazardous_asteroid,
        orbit_id = EXCLUDED.orbit_id,
        orbit_determination_date = EXCLUDED.orbit_determination_date,
        first_observation_date = EXCLUDED.first_observation_date,
        last_observation_date = EXCLUDED.last_observation_date,
        data_arc_in_days = EXCLUDED.data_arc_in_days,
        observations_used = EXCLUDED.observations_used,
        orbit_uncertainty = EXCLUDED.orbit_uncertainty,
        minimum_orbit_intersection = EXCLUDED.minimum_orbit_intersection,
        jupiter_tisserand_invariant = EXCLUDED.jupiter_tisserand_invariant,
        epoch_osculation = EXCLUDED.epoch_osculation,
        eccentricity = EXCLUDED.eccentricity,
        semi_major_axis = EXCLUDED.semi_major_axis,
        inclination = EXCLUDED.inclination,
        ascending_node_longitude = EXCLUDED.ascending_node_longitude,
        orbital_period = EXCLUDED.orbital_period,
        perihelion_distance = EXCLUDED.perihelion_distance,
        perihelion_argument = EXCLUDED.perihelion_argument,
        aphelion_distance = EXCLUDED.aphelion_distance,
        perihelion_time = EXCLUDED.perihelion_time,
        mean_anomaly = EXCLUDED.mean_anomaly,
        mean_motion = EXCLUDED.mean_motion,
        equinox = EXCLUDED.equinox,
        orbit_class_type = EXCLUDED.orbit_class_type,
        orbit_class_description = EXCLUDED.orbit_class_description,
        orbit_class_range = EXCLUDED.orbit_class_range,
        is_sentry_object = EXCLUDED.is_sentry_object;
        '''
        cur.executemany(asteroid_query, asteroid_data)

        # Insert Close Approach Data
        close_approach_query = '''
        INSERT INTO neo_data.close_approach_data (asteroid_id, close_approach_date, close_approach_date_full, epoch_date_close_approach,
        relative_velocity_kps, relative_velocity_kph, relative_velocity_mph, miss_distance_au, miss_distance_lunar,
        miss_distance_km, miss_distance_miles, orbiting_body)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (asteroid_id, close_approach_date) DO UPDATE SET
        close_approach_date_full = EXCLUDED.close_approach_date_full,
        epoch_date_close_approach = EXCLUDED.epoch_date_close_approach,
        relative_velocity_kps = EXCLUDED.relative_velocity_kps,
        relative_velocity_kph = EXCLUDED.relative_velocity_kph,
        relative_velocity_mph = EXCLUDED.relative_velocity_mph,
        miss_distance_au = EXCLUDED.miss_distance_au,
        miss_distance_lunar = EXCLUDED.miss_distance_lunar,
        miss_distance_km = EXCLUDED.miss_distance_km,
        miss_distance_miles = EXCLUDED.miss_distance_miles,
        orbiting_body = EXCLUDED.orbiting_body;
        '''
        cur.executemany(close_approach_query, close_approach_data)
    try:
        conn.commit()
        logger.info("Data upserted successfully.")
    except Exception as e:
        logger.error(f"Error upserting data: {e}")
        raise