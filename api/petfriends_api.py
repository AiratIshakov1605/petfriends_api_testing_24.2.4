# api/petfriends_api.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class PetFriendsAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.api_key = None

    def get_api_key(self):
        headers = {
            'email': os.getenv('EMAIL'),
            'password': os.getenv('PASSWORD'),
        }
        response = requests.get(f"{self.base_url}/api/key", headers=headers)
        if response.status_code == 200:
            self.api_key = response.json().get('key')
        return response

    def get_list_of_pets(self, filter=""):
        headers = {
            'auth_key': self.api_key
        }
        params = {
            'filter': filter
        }
        response = requests.get(f"{self.base_url}/api/pets", headers=headers, params=params)
        return response

    def add_new_pet(self, name, animal_type, age):
        headers = {
            'auth_key': self.api_key
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        response = requests.post(f"{self.base_url}/api/pets", headers=headers, data=data)
        return response

    def update_pet_info(self, pet_id, name, animal_type, age):
        headers = {
            'auth_key': self.api_key
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        response = requests.put(f"{self.base_url}/api/pets/{pet_id}", headers=headers, data=data)
        return response

    def delete_pet(self, pet_id):
        headers = {
            'auth_key': self.api_key
        }
        response = requests.delete(f"{self.base_url}/api/pets/{pet_id}", headers=headers)
        return response