from config.config import BASE_URL, ENDPOINTS
import requests

def get_breeds(headers):
    """Get all dog breeds"""
    url = f"{BASE_URL}/{ENDPOINTS['breeds']}"
    return requests.get(url, headers=headers)

def get_breed(headers, id):
    """Get specific dog breed"""
    url = f"{BASE_URL}/{ENDPOINTS['breeds']}/{id}"
    return requests.get(url, headers=headers)

