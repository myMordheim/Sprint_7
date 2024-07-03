import allure
import requests
from conftest import *
from const import *


class TestLoginCourier:
    @allure.title('Успешная авторизация')
    def test_login(self, helper_init):
        for_test = helper_init
        credentials = for_test.register_new_courier_and_return_login_password()
        payloda = {"login": credentials[0], "password": credentials[1]}
        response = requests.post(Endpoints.LOGIN, data=payloda)
        assert response.json() == {'id': response.json()['id']} and response.status_code == 200
        for_test.delete_courier(credentials[0], credentials[1])

    @allure.title('Возвращает ошибку, при некорректно пароле')
    def test_login_missing_password(self, helper_init):
        for_test = helper_init
        credentials = for_test.register_new_courier_and_return_login_password()
        payload = {"login": credentials[0], "password": ''}
        response = requests.post(Endpoints.LOGIN, data=payload)
        assert Response_message.missing_cred in response.text and response.status_code == 400
        for_test.delete_courier(credentials[0], credentials[1])

    @allure.title('Возвращает ошибку, при некорректном логине')
    def test_login_missing_login(self, helper_init):
        for_test = helper_init
        credentials = for_test.register_new_courier_and_return_login_password()
        payload = {"login": '', "password": credentials[1]}
        response = requests.post(Endpoints.LOGIN, data=payload)
        assert Response_message.missing_cred in response.text and response.status_code == 400
        for_test.delete_courier(credentials[0], credentials[1])

    @allure.title('Возвращает ошибку, при отправке пустых полей')
    def test_login_without_cred(self, helper_init):
        for_test = helper_init
        credentials = for_test.register_new_courier_and_return_login_password()
        payload = {"login": '', "password": ''}
        response = requests.post(Endpoints.LOGIN, data=payload)
        assert Response_message.missing_cred in response.text and response.status_code == 400
        for_test.delete_courier(credentials[0], credentials[1])

    @allure.title('Возвращает ошибку, при авторизации с некорректным паролем')
    def test_login_incorrect_password(self, helper_init):
        for_test = helper_init
        credentials = for_test.register_new_courier_and_return_login_password()
        payload = {"login": credentials[0], "password": Helper.generate_random_string(4)}
        response = requests.post(Endpoints.LOGIN, data=payload)
        assert Response_message.wrong_cred in response.text and response.status_code == 404
        for_test.delete_courier(credentials[0], credentials[1])

    @allure.title('Возвращает ошибку, при авторизации с некорректным логином')
    def test_login_incorrect_login(self, helper_init):
        for_test = helper_init
        credentials = for_test.register_new_courier_and_return_login_password()
        payload = {"login": credentials[0], "password": Helper.generate_random_string(4)}
        response = requests.post(Endpoints.LOGIN, data=payload)
        assert Response_message.wrong_cred in response.text and response.status_code == 404
        for_test.delete_courier(credentials[0], credentials[1])

    @allure.title('Возвращает ошибку, при авторизации несуществующего пользователя')
    def test_login_random_data(self):
        payload = {"login": Helper.generate_random_string(10), "password": Helper.generate_random_string(10)}
        response = requests.post(Endpoints.LOGIN, data=payload)
        assert Response_message.wrong_cred in response.text and response.status_code == 404
