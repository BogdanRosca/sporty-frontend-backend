import utils.breeds
from config.config import LABRADOR_ID

def test_get_all_breeds(auth_headers):
    response = utils.breeds.get_breeds(auth_headers)
    print(response)


def test_get_specific_breed(auth_headers):
    response = utils.breeds.get_breed(auth_headers, LABRADOR_ID)
    print(response)
