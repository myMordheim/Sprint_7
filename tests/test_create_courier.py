import pytest
import requests
from conftest import *
from const import *
class TestCreateCourier:

    def test_create_courier(self, helper_init):
        for_test = helper_init
        generate_data = for_test.generate_data()
        payload = {"login": generate_data[0], "password": generate_data[1], "firstname": generate_data[2]}
        response = requests.post(Endpoints.CREATE, data=payload)
        assert Response_message.positive_create in response.text and response.status_code == 201
        for_test.delete_courier(generate_data[0], generate_data[1])

    def test_double_create(self, helper_init):
        for_test = helper_init
        generate_data = for_test.generate_data()
        payload = {"login": generate_data[0], "password": generate_data[1], "firstname": generate_data[2]}
        requests.post(Endpoints.CREATE, data=payload)
        second_courier = requests.post(Endpoints.CREATE, data=payload)
        assert Response_message.double_courier_exception in second_courier.text and second_courier.status_code == 409
        for_test.delete_courier(generate_data[0], generate_data[1])

    def test_incorrect_credetional(self, helper_init):
        for_test = helper_init
        generate_data = for_test.generate_data()
        payload = {"login": generate_data[0]}
        response = requests.post(Endpoints.CREATE, data=payload)
        assert Response_message.missing_input in response.text and response.status_code == 400