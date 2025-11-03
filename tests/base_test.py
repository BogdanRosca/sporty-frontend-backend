"""
Base test class providing common functionality for all test classes
"""
import pytest
from config.config import LABRADOR_ID, IMAGE_IDS, USER_ID
from utils.test import load_test_data

class BaseTest:
    """Base class for all test classes with common setup and utilities"""
    
    @pytest.fixture(autouse=True)
    def setup_test_data(self, auth_headers):
        """Load common test data for all tests"""
        self.labrador_breed_id = LABRADOR_ID
        self.unexisting_breed_id = 1234
        self.labrador_response = load_test_data('labrador.json')
        self.auth_headers = auth_headers
        self.image_ids = IMAGE_IDS
        self.user_id = USER_ID

