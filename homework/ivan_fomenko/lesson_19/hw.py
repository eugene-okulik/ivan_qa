import requests
import json


BASE_URL = 'http://objapi.course.qa-practice.com'


def get_all_obj():
    response = requests.get(f'{BASE_URL}/object')
    obj_list = response.json()['data']

    assert response.status_code == 200, 'Status code is incorrect'
    print(f'Получено объектов: {len(obj_list)}')


def create_obj():
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
    assert response.json()['name'] == 'Ivan', 'Name is incorrect'
    assert response.json()['data']['age'] == 30, 'Age is incorrect'
    assert response.json()['data']['city'] == 'London', 'City is incorrect'

    return response.json()['id']


def get_one_obj():
    obj_id = create_obj()
    response = requests.get(f'{BASE_URL}/object/{obj_id}')
    print(f'Получен объект с id: {response.json()["id"]}')

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == obj_id, (
        f'Id is incorrect, expected {obj_id}, got {response.json()["id"]}'
    )
    assert response.json()['name'] == 'Ivan', 'Name is incorrect'
    assert response.json()['data']['age'] == 30, 'Age is incorrect'
    assert response.json()['data']['city'] == 'London', 'City is incorrect'

    print(f'Получен объект: {json.dumps(response.json(), indent=2)}')


def put_one_obj():
    obj_id = create_obj()
    body = {
        "name": "Ivan-UPD",
        "data": {
            "age": 31,
            "city": "London-UPD"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'{BASE_URL}/object/{obj_id}', json=body, headers=headers
    )
    print(f'Обновлен объект с id: {response.json()["id"]}')

    assert response.status_code == 200, 'Status code is incorrect'
    assert int(response.json()['id']) == int(obj_id), (
        f'Id is incorrect, expected {obj_id}, got {response.json()["id"]}'
    )
    assert response.json()['name'] == 'Ivan-UPD', 'Name is incorrect'
    assert response.json()['data']['age'] == 31, 'Age is incorrect'
    assert response.json()['data']['city'] == 'London-UPD', 'City is incorrect'


def patch_one_obj():
    obj_id = create_obj()
    body = {
        "name": "Ivan-PATCH"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'{BASE_URL}/object/{obj_id}', json=body, headers=headers
    )
    print(f'Патч объекта с id: {response.json()["id"]}')

    assert response.status_code == 200, 'Status code is incorrect'
    assert int(response.json()['id']) == int(obj_id), (
        f'Id is incorrect, expected {obj_id}, got {response.json()["id"]}'
    )
    assert response.json()['name'] == 'Ivan-PATCH', 'Name is incorrect'
    # проверяю, что не затерлись остальные данные
    assert response.json()['data']['age'] == 30, 'Age is incorrect'
    assert response.json()['data']['city'] == 'London', 'City is incorrect'


def delete_one_obj():
    obj_id = create_obj()
    response = requests.delete(f'{BASE_URL}/object/{obj_id}')

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.text == f'Object with id {obj_id} successfully deleted'
    print(f'Удален объект с id: {obj_id}')


get_all_obj()
create_obj()
get_one_obj()
put_one_obj()
patch_one_obj()
delete_one_obj()
