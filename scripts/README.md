# NEO Data Pipeline

## Overview
This project fetches Near-Earth Object (NEO) data from NASA's API and stores it into a PostgreSQL database.

## Structure
- `config.py`: API keys and database credentials.
- `fetch_data.py`: Fetches data from NASA API.
- `database.py`: Inserts/updates data into the database.
- `data_checks.py`: Validates data consistency.
- `logger.py`: Logs pipeline activities.
- `main.py`: Orchestrates the entire pipeline.

## Requirements
- Python 3.x
- PostgreSQL
- Required Python libraries: `requests`, `psycopg2`, `logging`

## How to Run
1. Update `config.py` with your API key and database credentials.
2. Set up the database using provided schema (not included here).
3. Run the pipeline:
   ```bash
   python main.py
