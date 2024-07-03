import requests
import pytest

from data import *
from conftest import *
from const import *


class TestCreateOrder:
    @pytest.mark.parametrize('colour',Data.colour_data)
    def test_create_order(self, colour, helper_init):
        for_test = helper_init
        response = for_test.create_order(colour)
        assert response.json() == {'track': response.json()['track']} and response.status_code == 201

    def test_return_list(self):
        response = requests.get(Endpoints.GET_ORDERS)
        assert response.status_code == 200 and type(response.json()['orders']) == list




