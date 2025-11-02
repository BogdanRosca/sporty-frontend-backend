from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

def test():
    response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key={API_KEY}&country=PA&year=2025&month=01&day=06")
    print(response.status_code)
    print(response.content)