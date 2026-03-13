import requests
import allure
from endpoints.main_class import MainApi


class PatchObj(MainApi):

    @allure.step('Send PATCH to upd obj by ID')
    def patch_obj(self, obj_id, name='Ivan-PATCH', headers=None):
        body = {
            "name": name
        }
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.BASE_URL}object/{obj_id}', json=body, headers=headers
        )
        return self.response
