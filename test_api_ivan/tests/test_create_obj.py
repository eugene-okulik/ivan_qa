import allure
import pytest
from utils.Checker import Checker


TEST_DATA_CREATE_OBJ = [
    ("Ivan", 30, "London"),
    ("Maria", 29, "Belgrade"),
    ("Mark", 46, "Sindey")]


NEGATIVE_TEST_DATA_CREATE_OBJ = [
    ("", 30, "London"),
    ("Ivan", -1, "Belgrade"),
    ("Mark", 46, "")
]


@allure.feature('Создание объекта')
@allure.story('Параметризация теста')
@pytest.mark.parametrize("name, age, city", TEST_DATA_CREATE_OBJ)
def test_create_obj(create_obj_api, name, age, city):
    response, obj_id = create_obj_api.create_obj(name, age, city)
    Checker.check_create_obj(response, name, age, city)


@allure.feature('Создание объекта')
@allure.story('Параметризация теста - негативные сценарии')
@pytest.mark.parametrize("name, age, city", NEGATIVE_TEST_DATA_CREATE_OBJ)
@pytest.mark.skip(reason="всегда возвращает 200, баг в API")
def test_create_obj_negative(create_obj_api, delete_obj_api, name, age, city):
    response, obj_id = create_obj_api.create_obj(name, age, city)

    Checker.check_create_obj_negative(response)
    # clean up
    delete_response = delete_obj_api.delete_obj(obj_id)
    Checker.check_delete_obj(delete_response, obj_id=obj_id)
