--DDL to create the tables for the NASA's NeoWs data
--Split the data into two tables where one has the details of the Asteroid and the other one has Close Approach data

CREATE TABLE IF NOT EXISTS asteroids (
    id TEXT PRIMARY KEY,
    name TEXT,
    neo_reference_id TEXT,
    absolute_magnitude_h REAL,
    estimated_diameter_min_km REAL,
    estimated_diameter_max_km REAL,
    estimated_diameter_mean_km REAL,
    is_potentially_hazardous_asteroid BOOLEAN,
    orbit_id TEXT,
    orbit_determination_date TEXT,
    first_observation_date TEXT,
    last_observation_date TEXT,
    data_arc_in_days INTEGER,
    observations_used INTEGER,
    orbit_uncertainty TEXT,
    minimum_orbit_intersection REAL,
    jupiter_tisserand_invariant REAL,
    epoch_osculation REAL,
    eccentricity REAL,
    semi_major_axis REAL,
    inclination REAL,
    ascending_node_longitude REAL,
    orbital_period REAL,
    perihelion_distance REAL,
    perihelion_argument REAL,
    aphelion_distance REAL,
    perihelion_time REAL,
    mean_anomaly REAL,
    mean_motion REAL,
    equinox TEXT,
    orbit_class_type TEXT,
    orbit_class_description TEXT,
    orbit_class_range TEXT,
    is_sentry_object BOOLEAN
);

CREATE TABLE IF NOT EXISTS close_approach_data (
    id SERIAL PRIMARY KEY,
    asteroid_id TEXT REFERENCES asteroids(id),
    close_approach_date TEXT,
    close_approach_date_full TEXT,
    epoch_date_close_approach BIGINT,
    relative_velocity_kps REAL,
    relative_velocity_kph REAL,
    relative_velocity_mph REAL,
    miss_distance_au REAL,
    miss_distance_lunar REAL,
    miss_distance_km REAL,
    miss_distance_miles REAL,
    orbiting_body TEXT
);

