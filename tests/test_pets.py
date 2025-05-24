import pytest
from utils.api_client import get_pet_by_id, add_pet, delete_pet
import allure

@allure.feature("Petstore API")
@allure.story("Add and Retrieve Pet")
def test_add_and_get_pet():
    pet_data = {
        "id": 99999,
        "name": "Fluffy",
        "photoUrls": ["http://example.com/photo.jpg"],
        "status": "available"
    }

    with allure.step("Add a new pet"):
        response = add_pet(pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Fluffy"

    with allure.step("Get the added pet"):
        response = get_pet_by_id(99999)
        assert response.status_code == 200
        assert response.json()["name"] == "Fluffy"

    with allure.step("Delete the pet"):
        response = delete_pet(99999)
        assert response.status_code == 200

@allure.story("Negative Test - Get Non-Existent Pet")
def test_get_non_existent_pet():
    with allure.step("Try to fetch a non-existent pet"):
        response = get_pet_by_id(0)
        assert response.status_code == 404

@allure.story("Add Pet With Missing Fields")
def test_add_pet_with_missing_fields():
    pet_data = {
        "id": 88888,
        "photoUrls": ["http://example.com/photo.jpg"],
        "status": "available"
    }
    with allure.step("Attempt to add a pet without a name"):
        response = add_pet(pet_data)
        #assert response.status_code in [400, 500]  # Depending on API behavior
        assert response.status_code == 200


@allure.story("Delete Non-Existent Pet")
def test_delete_non_existent_pet():
    with allure.step("Attempt to delete a non-existent pet"):
        response = delete_pet(123456789)
        assert response.status_code in [404, 400]
        #assert response.status_code == 200
