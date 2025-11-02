import utils.breeds
from tests.base_test import BaseTest
import allure 
from schemas.breads import DogBreedDetails

@allure.suite("v1/breeds")
class TestGetDogBreeds(BaseTest):
    """Test suite for getting dog breeds details"""

    def test_get_all_breeds(self):
        """Test getting all dog breeds with details"""
        response = utils.breeds.get_breeds(self.auth_headers).json()
        DogBreedDetails(**response[0])



    def test_get_specific_breed(self):
        """Test getting specific dog breed with details"""
        response = utils.breeds.get_breed(self.auth_headers, self.breed_id)
        print(response)
