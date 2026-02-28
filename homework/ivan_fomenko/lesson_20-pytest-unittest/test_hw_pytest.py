import requests
import pytest


BASE_URL = 'http://objapi.course.qa-practice.com'


@pytest.fixture(scope='session')
def inf_start_end():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def inf_test():
    print('before test')
    yield
    print('after test')


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


# тесты
def test_get_all_obj(inf_test, inf_start_end):
    response = requests.get(f'{BASE_URL}/object')
    obj_list = response.json()['data']

    assert response.status_code == 200, 'Status code is incorrect'
    print(f'Получено объектов: {len(obj_list)}')


@pytest.mark.parametrize("name, age, city", [
    ("Ivan", 30, "London"),
    ("Maria", 29, "Belgrade"),
    ("Mark", 46, "Sindey")
])
def test_create_obj(inf_test, name, age, city):
    body = {
        "name": name,
        "data": {
            "age": age,
            "city": city
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{BASE_URL}/object', json=body, headers=headers)
    print(f'Создан объект с id: {response.json()["id"]}')

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == name, 'Name is incorrect'
    assert response.json()['data']['age'] == age, 'Age is incorrect'
    assert response.json()['data']['city'] == city, 'City is incorrect'


def test_get_one_obj(inf_test, obj_id):
    response = requests.get(f'{BASE_URL}/object/{obj_id}')
    print(f'Получен объект с id: {response.json()["id"]}')

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == obj_id, (
        f'Id is incorrect, expected {obj_id}, got {response.json()["id"]}'
    )


@pytest.mark.critical
def test_put_one_obj(inf_test, obj_id):
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
    assert response.json()['name'] == body['name'], 'Name is incorrect'
    assert response.json()['data']['age'] == body['data']['age'], 'Age is incorrect'
    assert response.json()['data']['city'] == body['data']['city'], 'City is incorrect'


def test_patch_one_obj(inf_test, obj_id):
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


@pytest.mark.medium
def test_delete_one_obj(inf_test, inf_start_end, obj_id):
    response = requests.delete(f'{BASE_URL}/object/{obj_id}')

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.text == f'Object with id {obj_id} successfully deleted'
    print(f'Удален объект с id: {obj_id}')
