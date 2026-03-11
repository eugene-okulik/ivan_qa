import allure
from utils.Checker import Checker


@allure.feature('Редактирование объекта (PATCH)')
def test_patch_obj(patch_obj_api, created_obj):
    response = patch_obj_api.patch_obj(created_obj)

    Checker.check_patch_obj(response, obj_id=created_obj, name="Ivan-PATCH")
