from dotenv import load_dotenv
import pytest
import os

load_dotenv()

@pytest.fixture(scope="session")
def auth_headers():
    """Fixture that provides the API key for all tests."""
    headers = {
        "x-api-key": os.getenv('API_KEY')
    }
    return headers