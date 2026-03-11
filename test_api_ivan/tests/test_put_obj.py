import allure
import pytest
from utils.Checker import Checker


TEST_DATA_PUT_OBJ = [
    ("Ivan-PUT", 30, "London-PUT"),
    ("Maria-PUT", 29, "Belgrade-PUT"),
    ("Mark-PUT", 46, "Sindey-PUT")]


@allure.feature('Редактирование объекта')
@pytest.mark.parametrize("name, age, city", TEST_DATA_PUT_OBJ)
def test_put_obj(put_obj_api, created_obj, name, age, city):
    response = put_obj_api.put_obj(created_obj, name, age, city)

    Checker.check_put_obj(
        response, obj_id=created_obj, name=name, age=age, city=city
    )
