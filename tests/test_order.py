import requests
import pytest
import allure
from data import *
from conftest import *
from const import *


class TestCreateOrder:
    @allure.title('Создание заказа и получение его трек номера')
    @pytest.mark.parametrize('colour',Data.colour_data)
    def test_create_order(self, colour):
        response = Helper.create_order(colour)
        assert response.json() == {'track': response.json()['track']} and response.status_code == 201

    @allure.title('Получить список всех заказов')
    def test_return_list(self):
        response = requests.get(Endpoints.GET_ORDERS)
        assert response.status_code == 200 and type(response.json()['orders']) == list




