import pytest
from helper import *
from const import *


@pytest.fixture(scope="function")
def get_courier():
    courier = Helper.register_new_courier_and_return_login_password()
    yield courier
    if len(courier) == 3:
        courier_to_delete = Courier(courier)
        courier_to_delete.login()
        courier_to_delete.delete()
