import json

def load_test_data(filename):
    """Load test data from JSON file"""
    with open(f'data/{filename}') as f:
        return json.load(f)