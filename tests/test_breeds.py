from schemas.breads import DogBreedDetails
from tests.base_test import BaseTest
import allure 
import utils.breeds

@allure.suite("v1/breeds")
class TestGetDogBreeds(BaseTest):
    """Test suite for getting dog breeds details"""

    def test_get_all_breeds(self):
        """Test getting all dog breeds with details"""
        response = utils.breeds.get_breeds()
        
        assert response.status_code == 200

        response_json = response.json()[0]
        # Validate schema of first breed
        DogBreedDetails(**response_json)

        assert len(response_json) > 1

    def test_get_specific_breed(self):
        """Test getting specific dog breed with details"""
        response = utils.breeds.get_breed(self.labrador_breed_id)
        
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["bred_for"] == "Water retrieving"
        assert response_json["breed_group"] == "Sporting"
        assert response_json["height"]["imperial"] == "21.5 - 24.5"
        assert response_json["height"]["metric"] == "55 - 62"
        assert response_json["id"] == 149
        assert response_json["life_span"] == "10 - 13 years"
        assert response_json["name"] == "Labrador Retriever"
        assert response_json["reference_image_id"] == "B1uW7l5VX"
        assert response_json["temperament"] == "Kind, Outgoing, Agile, Gentle, Intelligent, Trusting, Even Tempered"
        assert response_json["weight"]["imperial"] == "55 - 80"
        assert response_json["weight"]["metric"] == "25 - 36"

    def test_get_unexisting_breed(self):
        """Test getting unexisting dog breed"""
        response = utils.breeds.get_breed(self.unexisting_breed_id)

        assert response.status_code == 400
        assert response.text == "INVALID_DATA"
