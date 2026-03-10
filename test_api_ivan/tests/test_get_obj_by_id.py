import allure
from utils.Checker import Checker


@allure.feature('Получение объекта по ID')
def test_get_obj_by_id(get_obj_by_id_api, create_obj_api, delete_obj_api):
    response, obj_id = create_obj_api.create_obj()
    response = get_obj_by_id_api.get_obj_by_id(obj_id)  

    Checker.check_get_obj_by_id(response, obj_id=obj_id)
    # Clean up
    delete_response = delete_obj_api.delete_obj(obj_id) 
    Checker.check_delete_obj(delete_response, obj_id=obj_id)
