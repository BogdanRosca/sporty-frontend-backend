"""Authentication utilities"""
import os
from dotenv import load_dotenv


def init_auth_env():
    """Load environment variables from a .env file."""
    load_dotenv()


def get_auth_headers():
    """Get authentication headers for API requests"""
    return {
        "x-api-key": os.getenv('API_KEY'),
        "Content-Type": "application/json"
    }
