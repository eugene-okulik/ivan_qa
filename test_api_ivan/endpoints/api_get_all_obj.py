import requests
import allure
from endpoints.main_class import MainApi


class GetAllObj(MainApi):

    @allure.step('Send GET to get all objects')
    def get_all_obj(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.BASE_URL}object')
        return self.response
