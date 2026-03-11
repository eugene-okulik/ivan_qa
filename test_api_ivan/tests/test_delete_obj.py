import allure
from utils.Checker import Checker


@allure.feature('Удаление объекта')
def test_delete_obj(delete_obj_api, created_obj):
    response = delete_obj_api.delete_obj(created_obj)

    Checker.check_delete_obj(response, obj_id=created_obj)
