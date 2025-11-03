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
        assert response_json["bred_for"] == self.labrador_response["bred_for"]
        assert response_json["breed_group"] == self.labrador_response["breed_group"]
        assert response_json["height"]["imperial"] == self.labrador_response["height"]["imperial"]
        assert response_json["height"]["metric"] == self.labrador_response["height"]["metric"]
        assert response_json["id"] == self.labrador_response["id"]
        assert response_json["life_span"] == self.labrador_response["life_span"]
        assert response_json["name"] == self.labrador_response["name"]
        assert response_json["reference_image_id"] == self.labrador_response["reference_image_id"]
        assert response_json["temperament"] == self.labrador_response["temperament"]
        assert response_json["weight"]["imperial"] == self.labrador_response["weight"]["imperial"]
        assert response_json["weight"]["metric"] == self.labrador_response["weight"]["metric"]

    def test_get_unexisting_breed(self):
        """Test getting unexisting dog breed"""
        response = utils.breeds.get_breed(self.unexisting_breed_id)

        assert response.status_code == 400
        assert response.text == "INVALID_DATA"
