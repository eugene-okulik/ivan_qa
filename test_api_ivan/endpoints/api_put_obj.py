import requests
import allure
from endpoints.main_class import MainApi


class PutObj(MainApi):
    @allure.step('Send PUT to update object by ID')
    def put_obj(
        self, obj_id, name='Ivan-PUT', age=20, city='London_PUT', headers=None
    ):
        body = {
            "name": name,
            "data": {
                "age": age,
                "city": city
            }
        }
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.BASE_URL}object/{obj_id}', json=body, headers=headers
        )
        return self.response
