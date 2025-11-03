from config.config import BASE_URL, ENDPOINTS
import requests

def get_favourites(headers :str = None):
    """Get all favourites images"""
    url = f"{BASE_URL}/{ENDPOINTS['favourites']}"
    return requests.get(url, headers=headers)

def save_favourite(img: str, headers :str = None ):
    """Save a favourite image"""
    if img:
        data = {"image_id": img}
    else:
        data = {}
    url = f"{BASE_URL}/{ENDPOINTS['favourites']}"
        
    return requests.post(url, headers=headers, json=data)

def remove_favourite(id: int, headers :str = None ):
    """Delete a favourite image"""
    url = f"{BASE_URL}/{ENDPOINTS['favourites']}/{id}"
    return requests.delete(url, headers=headers)

