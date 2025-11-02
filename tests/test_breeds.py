import utils.breeds
from tests.base_test import BaseTest

class TestGetDogBreeds(BaseTest):
    """Test suite for getting dog breeds details"""

    def test_get_all_breeds(self):
        response = utils.breeds.get_breeds(self.auth_headers)
        print(response)


    def test_get_specific_breed(self):
        response = utils.breeds.get_breed(self.auth_headers, self.breed_id)
        print(response)
