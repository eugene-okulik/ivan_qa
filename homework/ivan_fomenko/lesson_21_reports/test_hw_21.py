import requests
import pytest
import allure


BASE_URL = 'http://objapi.course.qa-practice.com'


@allure.title('Test available objects')
@allure.feature('Work with objects')
@allure.story('Get list of all objects')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.critical
def test_get_all_obj():
    with allure.step('get all objects'):
        response = requests.get(f'{BASE_URL}/object')
    obj_list = response.json()['data']

    with allure.step('check response'):
        assert response.status_code == 200, 'Status code is incorrect'
    print(f'Получено объектов: {len(obj_list)}')


@allure.title('Test create object')
@allure.feature('Work with objects')
@allure.story('Create new object')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("name, age, city", [
    ("Ivan", 30, "London"),
    ("Maria", 29, "Belgrade"),
    ("Mark", 46, "Sindey")
])
def test_create_obj(name, age, city):
    body = {
        "name": name,
        "data": {
            "age": age,
            "city": city
        }
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Create object'):
        response = requests.post(
            f'{BASE_URL}/object', json=body, headers=headers
        )
        print(f'Создан объект с id: {response.json()["id"]}')

    with allure.step('Check response'):
        print('Проверяем статус код и данные в ответе')
        assert response.status_code == 200, 'Status code is incorrect'
        assert int(response.json()['data']['age']) == int(age), (
            'Age is incorrect'
        )
        assert response.json()['name'] == name, 'Name is incorrect'
        assert response.json()['data']['city'] == city, 'City is incorrect'


@allure.title('Test get one object')
@allure.feature('Work with objects')
@allure.story('Get object by id')
@allure.severity(allure.severity_level.MINOR)
def test_get_one_obj(obj_id):
    with allure.step('Get object by id'):
        response = requests.get(f'{BASE_URL}/object/{obj_id}')
        print(f'Получен объект с id: {response.json()["id"]}')

    with allure.step('Check response'):
        assert response.status_code == 200, 'Status code is incorrect'
        assert response.json()['id'] == obj_id, (
            f'Id is incorrect, expected {obj_id}, got {response.json()["id"]}'
        )


@allure.title('Test update object')
@allure.feature('Work with objects')
@allure.story('Update object by id')
@allure.severity(allure.severity_level.NORMAL)
def test_put_one_obj(obj_id):
    body = {
        "name": "Ivan-UPD",
        "data": {
            "age": 31,
            "city": "London-UPD"
        }
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Update object by id'):
        response = requests.put(
            f'{BASE_URL}/object/{obj_id}', json=body, headers=headers
        )
        print(f'Обновлен объект с id: {response.json()["id"]}')

    with allure.step('Check response'):
        assert response.status_code == 200, 'Status code is incorrect'
        assert int(response.json()['id']) == int(obj_id), (
            f'Id is incorrect, expected {obj_id}, got {response.json()["id"]}'
        )
        assert response.json()['name'] == body['name'], 'Name is incorrect'
        assert response.json()['data']['age'] == body['data']['age'], (
            'Age is incorrect'
        )
        assert response.json()['data']['city'] == body['data']['city'], (
            'City is incorrect'
        )


def test_patch_one_obj(obj_id):
    body = {
        "name": "Ivan-PATCH"
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Patch object by id'):
        response = requests.patch(
            f'{BASE_URL}/object/{obj_id}', json=body, headers=headers
        )
        print(f'Патч объекта с id: {response.json()["id"]}')

    with allure.step('Check response'):
        assert response.status_code == 200, 'Status code is incorrect'
        assert int(response.json()['id']) == int(obj_id), (
            f'Id is incorrect, expected {obj_id}, got {response.json()["id"]}'
        )
        assert response.json()['name'] == 'Ivan-PATCH', 'Name is incorrect'
        # проверяю, что не затерлись остальные данные
        assert response.json()['data']['age'] == 30, 'Age is incorrect'
        assert response.json()['data']['city'] == 'London', 'City is incorrect'


@allure.title('Test delete object')
@allure.feature('Work with objects')
@allure.story('Delete object by id')
@allure.severity(allure.severity_level.MINOR)
def test_delete_one_obj(obj_id):
    with allure.step('Delete object by id'):
        response = requests.delete(f'{BASE_URL}/object/{obj_id}')

    with allure.step('Check response'):
        assert response.status_code == 200, 'Status code is incorrect'
        assert response.text == f'Object with id {obj_id} successfully deleted'
        print(f'Удален объект с id: {obj_id}')
