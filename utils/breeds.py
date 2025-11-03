from config.config import BASE_URL, ENDPOINTS
from utils.auth import get_auth_headers
import requests

def get_breeds():
    """Get all dog breeds"""
    url = f"{BASE_URL}/{ENDPOINTS['breeds']}"
    return requests.get(url, headers=get_auth_headers())

def get_breed(id: int):
    """Get specific dog breed"""
    url = f"{BASE_URL}/{ENDPOINTS['breeds']}/{id}"
    return requests.get(url, headers=get_auth_headers())

