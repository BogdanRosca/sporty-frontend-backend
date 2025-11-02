"""
Base test class providing common functionality for all test classes
"""
import pytest
from config.config import LABRADOR_ID
from utils.test import load_test_data

class BaseTest:
    """Base class for all test classes with common setup and utilities"""
    
    @pytest.fixture(autouse=True)
    def setup_test_data(self, auth_headers):
        """Load common test data for all tests"""
        self.breed_id = LABRADOR_ID
        self.labrador_response = load_test_data('labrador.json')
        self.auth_headers = auth_headers

