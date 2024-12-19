# data_checks.py
def validate_api_response(data):
    """
    Ensures the API response contains required fields.
    """
    if 'near_earth_objects' not in data:
        raise ValueError("Invalid API response: 'near_earth_objects' key missing")
