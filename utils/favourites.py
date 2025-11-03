from config.config import BASE_URL, ENDPOINTS
from utils.auth import get_auth_headers
import requests


def get_favourites():
    """Get all favourites images"""
    url = f"{BASE_URL}/{ENDPOINTS['favourites']}"
    return requests.get(url, headers=get_auth_headers())


def get_favourites_no_auth():
    """Get all favourites images"""
    url = f"{BASE_URL}/{ENDPOINTS['favourites']}"
    return requests.get(url)


def save_favourite(img: str):
    """Save a favourite image"""
    if img:
        data = {"image_id": img}
    else:
        data = {}
    url = f"{BASE_URL}/{ENDPOINTS['favourites']}"
    return requests.post(url, headers=get_auth_headers(), json=data)


def remove_favourite(id: int):
    """Delete a favourite image"""
    url = f"{BASE_URL}/{ENDPOINTS['favourites']}/{id}"
    return requests.delete(url, headers=get_auth_headers())
