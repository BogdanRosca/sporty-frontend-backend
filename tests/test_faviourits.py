from schemas.favourites import FavouriteImage
from tests.base_test import BaseTest
import allure 
import pytest
import utils.favourites


@allure.suite("v1/favourites")
class TestGetFavouriteImage(BaseTest):
    """Test suite for getting favourite breeds """
    
    @pytest.fixture(autouse=True)
    def start_clean(self):
        """Fixture that deletes all existing favourites at start of each test"""
        existing_favourits = utils.favourites.get_favourites().json()
        for favourite in existing_favourits:
            utils.favourites.remove_favourite(favourite["id"])

    def test_get_favourite_no_auth(self):
        """Test getting favourites images without autentication"""
        response = utils.favourites.get_favourites_no_auth()
        assert response.status_code == 401
        assert "AUTHENTICATION_ERROR" in response.text

    def test_get_favourite_not_created(self):
        """Test getting favourites images without creating first"""
        response = utils.favourites.get_favourites()
        assert response.status_code == 200
        assert response.json() == []

    def test_get_one_existing_faviourite(self):
        """Test getting favourites images after creating faviourit"""
        IMAGE_ID = self.image_ids[0]

        create_response = utils.favourites.save_favourite(IMAGE_ID)
        assert create_response.status_code == 200
        
        response = utils.favourites.get_favourites()
        assert response.status_code == 200

        response_json = response.json()[0]
        FavouriteImage(**response_json)
        assert response_json["user_id"] == self.user_id
        assert response_json["image_id"] == IMAGE_ID
        assert response_json["image"]["id"] == IMAGE_ID
        assert response_json["image"]["url"] == f"https://cdn2.thedogapi.com/images/{IMAGE_ID}.jpg" 

    def test_get_multiple_existing_favourites(self):
        """Test getting favourites images after creating favourites"""
        IMAGE_ID_1 = self.image_ids[0]
        IMAGE_ID_2 = self.image_ids[1]
        
        create_response = utils.favourites.save_favourite(IMAGE_ID_1)
        assert create_response.status_code == 200

        create_response = utils.favourites.save_favourite(IMAGE_ID_2)
        assert create_response.status_code == 200
        
        response = utils.favourites.get_favourites()
        assert response.status_code == 200

        response_json = response.json()[0]
        FavouriteImage(**response_json)
        assert response_json["user_id"] == self.user_id
        assert response_json["image_id"] == IMAGE_ID_1
        assert response_json["image"]["id"] == IMAGE_ID_1
        assert response_json["image"]["url"] == f"https://cdn2.thedogapi.com/images/{IMAGE_ID_1}.jpg" 

        response_json = response.json()[1]
        FavouriteImage(**response_json)
        assert response_json["user_id"] == self.user_id
        assert response_json["image_id"] == IMAGE_ID_2
        assert response_json["image"]["id"] == IMAGE_ID_2
        assert response_json["image"]["url"] == f"https://cdn2.thedogapi.com/images/{IMAGE_ID_2}.jpg" 

    def test_create_favourite_no_body(self):
        """Test adding a favourites image without body"""
        response = utils.favourites.save_favourite(None)
        assert response.status_code == 400
        assert response.text == '"image_id" is required'

    def test_create_favourite(self):
        """Test adding a favourites image"""
        IMAGE_ID = self.image_ids[0]
        response = utils.favourites.save_favourite(IMAGE_ID)
        assert response.status_code == 200

        response_json = response.json()
        assert response_json["message"] == "SUCCESS"
        
    def test_delete_favourite(self):
        """Test removing a favourite image"""
        IMAGE_ID = self.image_ids[0]

        response = utils.favourites.save_favourite(IMAGE_ID)
        assert response.status_code == 200
        new_favourite_id = response.json()["id"]

        response = utils.favourites.remove_favourite(new_favourite_id)
        assert response.status_code == 200

        response_json = response.json()
        assert response_json["message"] == "SUCCESS"

        
        
       
