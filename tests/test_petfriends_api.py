# tests/test_petfriends_api.py

import pytest
from api.petfriends_api import PetFriendsAPI

@pytest.fixture
def api():
    api = PetFriendsAPI("https://petfriends.skillfactory.ru")
    api.get_api_key()
    return api

def test_get_api_key(api):
    response = api.get_api_key()
    assert response.status_code == 200
    assert 'key' in response.json()

def test_get_list_of_pets(api):
    response = api.get_list_of_pets()
    assert response.status_code == 200
    assert len(response.json().get('pets')) > 0

def test_add_new_pet(api):
    response = api.add_new_pet("Buddy", "dog", "3")
    assert response.status_code == 200
    assert response.json().get('name') == "Buddy"

def test_update_pet_info(api):
    # First, add a new pet
    add_response = api.add_new_pet("Buddy", "dog", "3")
    pet_id = add_response.json().get('id')

    # Then, update the pet info
    response = api.update_pet_info(pet_id, "Buddy Jr.", "dog", "4")
    assert response.status_code == 200
    assert response.json().get('name') == "Buddy Jr."

def test_delete_pet(api):
    # First, add a new pet
    add_response = api.add_new_pet("Buddy", "dog", "3")
    pet_id = add_response.json().get('id')

    # Then, delete the pet
    response = api.delete_pet(pet_id)
    assert response.status_code == 200

def test_get_list_of_pets_with_filter(api):
    response = api.get_list_of_pets("my_pets")
    assert response.status_code == 200
    assert len(response.json().get('pets')) >= 0

def test_add_new_pet_without_photo(api):
    response = api.add_new_pet("Buddy", "dog", "3")
    assert response.status_code == 200
    assert response.json().get('name') == "Buddy"

def test_update_pet_info_with_invalid_id(api):
    response = api.update_pet_info("invalid_id", "Buddy Jr.", "dog", "4")
    assert response.status_code == 400  # Assuming the API returns 400 for invalid ID

def test_delete_pet_with_invalid_id(api):
    response = api.delete_pet("invalid_id")
    assert response.status_code == 400  # Assuming the API returns 400 for invalid ID

def test_get_api_key_with_invalid_credentials(api):
    api.api_key = None
    response = api.get_api_key()
    assert response.status_code == 403  # Assuming the API returns 403 for invalid credentials