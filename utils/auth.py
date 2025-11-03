"""Authentication utilities"""
import os
from dotenv import load_dotenv

load_dotenv()

def get_auth_headers():
    """Get authentication headers for API requests"""
    return {
        "x-api-key": os.getenv('API_KEY'),
        "Content-Type": "application/json"
    }