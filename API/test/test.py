import requests
import allure
import pytest

URL = "https://petstore.swagger.io/v2/"

@pytest.fixture
def pet_id():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Charles",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Golden retriever"
            }
        ],
        "status": "available"
    }

    response = requests.post(url=f'{URL}pet', json=payload).json()
    yield response['id']

    # delete after finishing the test
    requests.delete(url=f'{URL}pet/{pet_id}')


@allure.title("Creating a pet")
def test_create_pet():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Charles",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Golden retriever"
            }
        ],
        "status": "available"
    }

    response = requests.post(url=f'{URL}pet', json=payload)
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']

@allure.title("Updating a pet")
def test_update_pet(pet_id):
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Borya",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Golden retriever"
            }
        ],
        "status": "available"
    }
    response = requests.put(url=f'{URL}pet', json=payload)
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']


@allure.title("Finding pets by status")
def test_find_by_status():
    response = requests.get(url=f'{URL}pet/findByStatus', params={'status': 'available'})
    assert response.status_code == 200
    available_pets = response.json()
    for pet in available_pets:
        assert pet['status'] == 'available'

    response = requests.get(url=f'{URL}pet/findByStatus', params={'status': 'pending'})
    assert response.status_code == 200
    pending_pets = response.json()
    for pet in pending_pets:
        assert pet['status'] == 'pending'

    response = requests.get(url=f'{URL}pet/findByStatus', params={'status': 'sold'})
    assert response.status_code == 200
    sold_pets = response.json()
    for pet in sold_pets:
        assert pet['status'] == 'sold'




@allure.title("Finding pets by id")
def test_find_by_id(pet_id):
    response = requests.get(url=f'{URL}pet/{pet_id}')
    assert response.status_code == 200
    assert response.json()['id'] == pet_id
    assert response.json()['name'] == 'Charles'


allure.title('Deleting pet')
def test_pet_delete():
    pet_id = test_create_pet
    response = requests.delete(url=f'{URL}pet/{pet_id}')
    assert response.status_code == 404
 def



