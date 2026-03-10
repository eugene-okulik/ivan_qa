import requests
import allure
from endpoints.main_class import MainApi


class DeleteObj(MainApi):

    @allure.step('Send DELETE to delete object by ID')
    def delete_obj(self, obj_id):
        self.response = requests.delete(
            f'{self.BASE_URL}object/{obj_id}'
        )
        return self.response
