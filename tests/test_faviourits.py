import requests

# No auth 
# No faviorit 

def test_favourits(auth_headers):
    response = requests.get(f"https://api.thedogapi.com/v1/favourites", headers=auth_headers)
    print(response.status_code)
    print(response.content)

