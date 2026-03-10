import pytest
from endpoints.api_create_obj import CreateObj
from endpoints.api_get_all_obj import GetAllObj
from endpoints.api_get_obj_by_id import GetObjById
from endpoints.api_delete_obj import DeleteObj
from endpoints.api_put_obj import PutObj
from endpoints.api_patch_obj import PatchObj


@pytest.fixture(scope='function')
def create_obj_api():
    return CreateObj()


@pytest.fixture(scope='function')
def get_all_obj_api():
    return GetAllObj()


@pytest.fixture(scope='function')
def get_obj_by_id_api():
    return GetObjById()


@pytest.fixture(scope='function')
def delete_obj_api():
    return DeleteObj()


@pytest.fixture(scope='function')
def put_obj_api():
    return PutObj()


@pytest.fixture(scope='function')
def patch_obj_api():
    return PatchObj()
