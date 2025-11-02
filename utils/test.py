import json

def load_test_data(filename):
    """Load test data from JSON file"""
    try:
        with open(f'data/{filename}') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Test data file 'data/{filename}' not found.")