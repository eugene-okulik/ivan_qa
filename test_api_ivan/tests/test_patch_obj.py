import allure
from utils.Checker import Checker


@allure.feature('Редактирование объекта (PATCH)')
def test_patch_obj(patch_obj_api, create_obj_api, delete_obj_api):
    response, obj_id = create_obj_api.create_obj()
    patch_response = patch_obj_api.patch_obj(obj_id, name="Ivan-PATCH")

    Checker.check_patch_obj(patch_response, obj_id=obj_id, name="Ivan-PATCH")

    # Clean up
    delete_response = delete_obj_api.delete_obj(obj_id)
    Checker.check_delete_obj(delete_response, obj_id=obj_id)
