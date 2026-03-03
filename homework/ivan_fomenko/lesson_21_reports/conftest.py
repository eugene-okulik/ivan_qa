import pytest
import requests


BASE_URL = 'http://objapi.course.qa-practice.com'


@pytest.fixture(scope='function')
def obj_id():
    body = {
        "name": "Ivan",
        "data": {
            "age": 30,
            "city": "London"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{BASE_URL}/object', json=body, headers=headers)
    print(f'Создан объект с id: {response.json()["id"]}')
    assert response.status_code == 200, 'Status code is incorrect'
    obj_id_value = response.json()["id"]

    yield obj_id_value
    print(f'Deleting obj id: {obj_id_value}..')
    requests.delete(f'{BASE_URL}/object/{obj_id_value}')
    print(f'Obj id:{obj_id_value} delete succesefull')
