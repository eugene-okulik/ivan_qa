import allure


class Checker:

    @staticmethod
    @allure.step('Check response')
    def check_create_obj(response, name, age, city):
        with allure.step('Проверка ответа'):
            print('Проверяем статус код и данные в ответе')
            assert response.status_code == 200, 'Status code is incorrect'
            assert response.json()['name'] == name, 'Name is incorrect'
            assert response.json()['data']['age'] == age, 'Age is incorrect'
            assert response.json()['data']['city'] == city, 'City is incorrect'

    @staticmethod
    @allure.step('Check response for negative test')
    def check_create_obj_negative(response):
        with allure.step('Проверка ответа'):
            print('Проверяем статус код и данные в ответе')
            assert response.status_code == 400, (
                f'Status code is incorrect got {response.status_code}'
            )

    @staticmethod
    @allure.step('Check response for get all objects')
    def check_get_all_obj(response):
        with allure.step('Проверка ответа'):
            print('Проверяем статус код и данные в ответе')
            assert response.status_code == 200, 'Status code is incorrect'
            assert isinstance(response.json(), dict), (
                f'Response is not a list. Got {type(response.json())}'
            )

    @staticmethod
    @allure.step('Check response for get object by id')
    def check_get_obj_by_id(response, obj_id):
        with allure.step('Проверка ответа'):
            print('Проверяем статус код и данные в ответе')
            assert response.status_code == 200, 'Status code is incorrect'
            assert response.json()['id'] == obj_id, (
                f'Id is incorrect, expected {obj_id},'
                f'got {response.json()["id"]}'
            )

    @staticmethod
    @allure.step('Check response for delete object')
    def check_delete_obj(response, obj_id=None):
        with allure.step('Проверка ответа'):
            print('Проверяем статус код и данные в ответе')
            assert response.status_code == 200, 'Status code is incorrect'
            assert response.text == (
                f'Object with id {obj_id} successfully deleted'
            ), (
                f'expected msg "Object with id {obj_id} successfully deleted",'
                f'got "{response.text}"'
            )

    @staticmethod
    @allure.step('Check response for update object')
    def check_put_obj(response, obj_id, name, age, city):
        with allure.step('Проверка ответа'):
            print('Проверяем статус код и данные в ответе')
            assert response.status_code == 200, 'Status code is incorrect'
            assert int(response.json()['id']) == int(obj_id), (
                f'Id is incorrect, expected {obj_id},'
                f'got {response.json()["id"]}'
            )
            assert response.json()['name'] == name, 'Name is incorrect'
            assert response.json()['data']['age'] == age, 'Age is incorrect'
            assert response.json()['data']['city'] == city, 'City is incorrect'

    @staticmethod
    @allure.step('Check response for patch object')
    def check_patch_obj(response, obj_id, name):
        with allure.step('Проверка ответа'):
            assert response.status_code == 200, 'Status code is incorrect'
            assert int(response.json()['id']) == int(obj_id), (
                f'Id is incorrect, expected {obj_id},'
                f'got {response.json()["id"]}'
            )
            assert response.json()['name'] == 'Ivan-PATCH', 'Name is incorrect'
            # проверяю, что не затерлись остальные данные
            assert response.json()['data']['age'] == 20, (
                'Age is incorrect'
            )
            assert response.json()['data']['city'] == 'Budva', (
                'City is incorrect'
            )
