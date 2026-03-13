import allure
from utils.Checker import Checker


@allure.feature('Получение всех объектов')
def test_get_all_obj(get_all_obj_api):
    response = get_all_obj_api.get_all_obj()

    Checker.check_get_all_obj(response)
