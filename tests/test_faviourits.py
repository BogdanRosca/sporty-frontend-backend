from tests.base_test import BaseTest
from schemas.favourites import FavouriteImage
import allure 
import utils.favourites
import pytest


@allure.suite("v1/faviourits")
class TestGetFavouriteImage(BaseTest):
    """Test suite for getting favourite breeds """
    
    @pytest.fixture(autouse=True)
    def start_clean(self):
        """Fixture that deletes all exisring favourites at start of each test"""
        existing_favourits = utils.favourites.get_favourites(self.auth_headers).json()
        for favourite in existing_favourits:
            utils.favourites.remove_favourite(favourite["id"], self.auth_headers)

    def test_get_favourite_no_auth(self):
        """Test getting faviourits images without autentication"""
        response = utils.favourites.get_favourites()
        assert response.status_code == 401
        assert "AUTHENTICATION_ERROR" in response.text

    def test_get_favourite_not_created(self):
        """Test getting faviourits images without creating first"""
        response = utils.favourites.get_favourites(self.auth_headers)
        assert response.status_code == 200
        assert response.json() == []

    def test_get_faviourite_one_existing(self):
        """Test getting faviourits images after creating faviourit"""
        create_response = utils.favourites.save_favourite(self.image_id, self.auth_headers)
        assert create_response.status_code == 200
        
        response = utils.favourites.get_favourites(self.auth_headers)
        assert response.status_code == 200

        response_json = response.json()[0]
        FavouriteImage(**response_json)
        assert response_json["user_id"] == self.user_id
        assert response_json["image_id"] == self.image_id
        assert response_json["image"]["id"] == self.image_id
        assert response_json["image"]["url"] == f"https://cdn2.thedogapi.com/images/{self.image_id}.jpg" 

    def test_create_favourite_no_body(self):
        """Test adding a faviourits image without body"""
        response = utils.favourites.save_favourite(None, self.auth_headers)
        assert response.status_code == 400
        assert response.text == '"image_id" is required'

    def test_create_favourite(self):
        """Test adding a faviourits image"""
        response = utils.favourites.save_favourite(self.image_id, self.auth_headers)
        assert response.status_code == 200

        response_json = response.json()
        assert response_json["message"] == "SUCCESS"
        
    def test_delete_favourite(self):
        """Test removing a faviourit image"""
        response = utils.favourites.save_favourite(self.image_id, self.auth_headers)
        assert response.status_code == 200
        id = response.json()["id"]

        response = utils.favourites.remove_favourite(id, self.auth_headers)
        assert response.status_code == 200

        response_json = response.json()
        assert response_json["message"] == "SUCCESS"

        
        
       
