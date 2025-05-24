import pytest
from utils.api_client import place_order, get_order_by_id, delete_order, get_inventory
import allure

@allure.feature("Store API")
@allure.story("Place and Get Order")
def test_place_and_get_order():
    order_data = {
        "id": 1001,
        "petId": 99999,
        "quantity": 1,
        "shipDate": "2025-05-24T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }

    with allure.step("Place an order"):
        response = place_order(order_data)
        assert response.status_code == 200
        assert response.json()["id"] == 1001

    with allure.step("Get the placed order"):
        response = get_order_by_id(1001)
        assert response.status_code == 200
        assert response.json()["id"] == 1001

    with allure.step("Delete the order"):
        response = delete_order(1001)
        assert response.status_code == 200

@allure.story("Get Inventory")
def test_get_inventory():
    response = get_inventory()
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

@allure.story("Get Non-Existent Order")
def test_get_non_existent_order():
    response = get_order_by_id(0)
    assert response.status_code == 404

@allure.story("Delete Non-Existent Order")
def test_delete_non_existent_order():
    response = delete_order(0)
    assert response.status_code in [400, 404]
