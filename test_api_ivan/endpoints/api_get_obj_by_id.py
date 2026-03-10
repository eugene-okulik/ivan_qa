import requests
import allure
from endpoints.main_class import MainApi


class GetObjById(MainApi):

    @allure.step('Send GET to get object by ID')
    def get_obj_by_id(self, obj_id):
        self.response = requests.get(
            f'{self.BASE_URL}object/{obj_id}'
        )
        return self.response
