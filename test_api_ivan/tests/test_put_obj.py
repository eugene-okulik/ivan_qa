import allure
import pytest
from utils.Checker import Checker


TEST_DATA_PUT_OBJ = [
    ("Ivan-PUT", 30, "London-PUT"),
    ("Maria-PUT", 29, "Belgrade-PUT"),
    ("Mark-PUT", 46, "Sindey-PUT")]


@allure.feature('Редактирование объекта')
@pytest.mark.parametrize("name, age, city", TEST_DATA_PUT_OBJ)
def test_put_obj(put_obj_api, create_obj_api, delete_obj_api, name, age, city):
    response, obj_id = create_obj_api.create_obj()
    put_response = put_obj_api.put_obj(obj_id, name, age, city)

    Checker.check_put_obj(
        put_response, obj_id=obj_id, name=name, age=age, city=city
    )

    # Clean up
    delete_response = delete_obj_api.delete_obj(obj_id)
    Checker.check_delete_obj(delete_response, obj_id=obj_id)
