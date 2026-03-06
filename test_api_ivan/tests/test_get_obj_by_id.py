import allure
from utils.Checker import Checker


@allure.feature('Получение объекта по ID')
def test_get_obj_by_id(delete_obj_endpoint, post_create_obj_endpoint):
    # Сначала создаем объект, чтобы получить его ID
    create_response = post_create_obj_endpoint.api_create_obj()
    obj_id = create_response.json()['id']

    response = delete_obj_endpoint.api_delete_obj(obj_id)
    Checker.check_delete_obj(response, obj_id)
