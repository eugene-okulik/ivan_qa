import pytest
from endpoints.api_create_obj import CreateObj
from endpoints.api_get_all_obj import GetAllObj
from endpoints.api_get_obj_by_id import GetObjById
from endpoints.api_delete_obj import DeleteObj


@pytest.fixture(scope='function')
def post_create_obj_endpoint():
    return CreateObj()


@pytest.fixture(scope='function')
def get_all_obj_endpoint():
    return GetAllObj()


@pytest.fixture(scope='function')
def get_obj_by_id_endpoint():
    return GetObjById()


@pytest.fixture(scope='function')
def delete_obj_endpoint():
    return DeleteObj()
