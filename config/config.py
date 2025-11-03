"""
Configuration file for API test framework
"""

BASE_URL = 'https://api.thedogapi.com'

DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

ENDPOINTS = {
    'breeds': 'v1/breeds',
    'favourites': 'v1/favourites',
}

LABRADOR_ID = 149

IMAGE_ID = 'BJa4kxc4X'

USER_ID = 'h5qfir'