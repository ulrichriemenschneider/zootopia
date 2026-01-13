import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
        ...
    },
    'locations': [
        ...
    ],
    'characteristics': {
        ...
    }
    },
    """
    url = f"{REQUEST_URL}{animal_name}"
    res = requests.get(url, headers={"X-Api-Key": API_KEY})
    if res.status_code == requests.codes.ok:
        print("Success:", res.status_code)
        return res.json()
    else:
        print("Error:", res.status_code, res.text)
        return None
