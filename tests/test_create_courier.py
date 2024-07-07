import allure
import pytest
import requests
from conftest import *
from const import *


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    def test_create_courier(self):
        generate_data = Helper.generate_data()
        payload = {"login": generate_data[0], "password": generate_data[1], "firstname": generate_data[2]}
        response = requests.post(Endpoints.CREATE, data=payload)
        assert Response_message.positive_create in response.text and response.status_code == 201
        Helper.delete_courier(generate_data[0], generate_data[1])

    @allure.title('Возвращает ошибку, при создании дубля')
    def test_double_create(self):
        generate_data = Helper.generate_data()
        payload = {"login": generate_data[0], "password": generate_data[1], "firstname": generate_data[2]}
        requests.post(Endpoints.CREATE, data=payload)
        second_courier = requests.post(Endpoints.CREATE, data=payload)
        assert Response_message.double_courier_exception in second_courier.text and second_courier.status_code == 409
        Helper.delete_courier(generate_data[0], generate_data[1])

    @allure.title('Возвращает ошибку, при использовании некорректных кредов')
    def test_incorrect_credetional(self):
        generate_data = Helper.generate_data()
        payload = {"login": generate_data[0]}
        response = requests.post(Endpoints.CREATE, data=payload)
        assert Response_message.missing_input in response.text and response.status_code == 400
