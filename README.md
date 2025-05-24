# Petstore API Test Automation Framework

This framework uses **Pytest** and **Allure Reports** to test the Swagger Petstore API, including Pets, Store, and User modules. It supports JSON-based data-driven testing for user-related scenarios.

## 📁 Project Structure

```
petstore_api_test/
├── data/
│   └── users.json               # Test data for user API
├── tests/
│   ├── test_pets.py            # Pet API test cases
│   ├── test_store.py           # Store API test cases
│   └── test_user.py            # User API tests (data-driven)
├── utils/
│   └── api_client.py           # API wrappers
├── conftest.py                 # Adds project root to PYTHONPATH
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration
└── README.md                   # This file
```

## ✅ Features

- **Pet API:** Add, get, delete pets
- **Store API:** Order management and inventory
- **User API:** Create, fetch, delete users
- **Data-driven testing:** JSON input for User API
- **Allure Reports:** Detailed, interactive test results

## 🚀 How to Run

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Environment

- Windows:
  ```bash
  venv\Scripts\activate
  ```

- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Tests

```bash
pytest
```

Or with Allure results:

```bash
pytest --alluredir=allure-results
```

### 5. View Allure Report

Make sure Allure CLI is installed. Then:

```bash
allure serve allure-results
```

## 📊 Sample User Test Data

See `data/users.json` for sample input:

```json
[
  {
    "id": 3001,
    "username": "userone",
    "firstName": "User",
    "lastName": "One",
    "email": "userone@example.com",
    "password": "pass123",
    "phone": "1111111111",
    "userStatus": 1
  }
]
```

You can extend this list to cover more test scenarios.
