import requests
import allure
from endpoints.main_class import MainApi


class CreateObj(MainApi):

    @allure.step('Send POST to create object')
    def create_obj(self, name='Ivan', age=20, city='Budva', headers=None):
        body = {
            "name": name,
            "data": {
                "age": age,
                "city": city
            }
        }
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.BASE_URL}object', json=body, headers=headers
        )
        obj_id = self.response.json().get('id')
        return self.response, obj_id
