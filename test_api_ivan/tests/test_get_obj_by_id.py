import allure
from utils.Checker import Checker


@allure.feature('Получение объекта по ID')
def test_get_obj_by_id(get_obj_by_id_api, created_obj):
    response = get_obj_by_id_api.get_obj_by_id(created_obj)

    Checker.check_get_obj_by_id(response, obj_id=created_obj)
