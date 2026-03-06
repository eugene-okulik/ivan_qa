import allure
from utils.Checker import Checker


@allure.feature('Получение всех объектов')
def test_get_all_obj(get_all_obj_endpoint):
    response = get_all_obj_endpoint.api_get_all_obj()

    Checker.check_get_all_obj(response)
