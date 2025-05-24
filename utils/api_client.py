import requests

BASE_URL = "https://petstore.swagger.io/v2"

def get_pet_by_id(pet_id):
    return requests.get(f"{BASE_URL}/pet/{pet_id}")

def add_pet(payload):
    headers = {"Content-Type": "application/json"}
    return requests.post(f"{BASE_URL}/pet", json=payload, headers=headers)

def delete_pet(pet_id):
    return requests.delete(f"{BASE_URL}/pet/{pet_id}")

def place_order(payload):
    headers = {"Content-Type": "application/json"}
    return requests.post(f"{BASE_URL}/store/order", json=payload, headers=headers)

def get_order_by_id(order_id):
    return requests.get(f"{BASE_URL}/store/order/{order_id}")

def delete_order(order_id):
    return requests.delete(f"{BASE_URL}/store/order/{order_id}")

def get_inventory():
    return requests.get(f"{BASE_URL}/store/inventory")


def create_user(payload):
    headers = {"Content-Type": "application/json"}
    return requests.post(f"{BASE_URL}/user", json=payload, headers=headers)

def get_user_by_username(username):
    return requests.get(f"{BASE_URL}/user/{username}")

def delete_user(username):
    return requests.delete(f"{BASE_URL}/user/{username}")
