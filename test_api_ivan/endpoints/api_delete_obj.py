import requests
import allure
from endpoints.main_class import MainApi


class DeleteObj(MainApi):

    @allure.step('Send DELETE to delete object')
    def api_delete_obj(self, obj_id):
        self.response = requests.delete(
            f'{self.BASE_URL}object/{obj_id}', headers=self.headers
        )
        return self.response
