import pytest
from helper import *
from const import *


@pytest.fixture(scope="function")
def helper_init():
    return Helper


@pytest.fixture(scope="function")
def get_courier(Helper):
    payload = Helper.register_new_courier_and_return_login_password()
    response = requests.post(Endpoints.LOGIN, data={"login": payload[0], "password": payload[1]})
    courier_id = response.json()['id']
    yield courier_id
    requests.delete(f'{Endpoints.DELETE}/{courier_id}')
