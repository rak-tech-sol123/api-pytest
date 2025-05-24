import pytest
import json
import allure
from utils.api_client import create_user, get_user_by_username, delete_user

def load_user_data():
    with open("data/users.json", "r") as f:
        return json.load(f)

@allure.feature("User API")
@allure.story("Create/Get/Delete User - Data Driven")
@pytest.mark.parametrize("user", load_user_data())
def test_user_crud_from_json(user):
    username = user["username"]

    with allure.step(f"Create user {username}"):
        response = create_user(user)
        assert response.status_code == 200

    with allure.step(f"Get user {username}"):
        response = get_user_by_username(username)
        assert response.status_code == 200
        assert response.json()["username"] == username

    with allure.step(f"Delete user {username}"):
        response = delete_user(username)
        assert response.status_code == 200
