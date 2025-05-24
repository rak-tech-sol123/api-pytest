import pytest
from utils.api_client import create_user, get_user_by_username, delete_user
import allure

@allure.feature("User API")
@allure.story("Create, Get and Delete User")
def test_create_get_delete_user():
    user_data = {
        "id": 2001,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }

    response = create_user(user_data)
    assert response.status_code == 200

    response = get_user_by_username("testuser")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

    response = delete_user("testuser")
    assert response.status_code == 200

@allure.story("Get Non-Existent User")
def test_get_non_existent_user():
    response = get_user_by_username("nonexistentuser123")
    assert response.status_code == 404

@allure.story("Delete Non-Existent User")
def test_delete_non_existent_user():
    response = delete_user("nonexistentuser123")
    assert response.status_code in [400, 404]
