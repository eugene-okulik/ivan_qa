import allure
from utils.Checker import Checker


@allure.feature('Удаление объекта')
def test_delete_obj(delete_obj_api, create_obj_api):
    response, obj_id = create_obj_api.create_obj()
    delete_response = delete_obj_api.delete_obj(obj_id)

    Checker.check_delete_obj(delete_response, obj_id=obj_id)
