import allure
import requests
from conftest import *
from const import *


class TestLoginCourier:
    @allure.title('Успешная авторизация')
    def test_login(self, get_courier):
        courier = Courier(get_courier)
        response = courier.login()
        assert response.json() == {'id': response.json()['id']} and response.status_code == 200


    @allure.title('Возвращает ошибку, при некорректно пароле')
    def test_login_missing_password(self,get_courier):
        courier = Courier([get_courier[0], '', get_courier[2]])
        response = courier.login()
        assert Response_message.missing_cred in response.text and response.status_code == 400


    @allure.title('Возвращает ошибку, при некорректном логине')
    def test_login_missing_login(self, get_courier):
        courier = Courier(['', get_courier[1], get_courier[2]])
        response = courier.login()
        assert Response_message.missing_cred in response.text and response.status_code == 400


    @allure.title('Возвращает ошибку, при отправке пустых полей')
    def test_login_without_cred(self, get_courier):
        courier = Courier(['', '', ''])
        response = courier.login()
        assert Response_message.missing_cred in response.text and response.status_code == 400


    @allure.title('Возвращает ошибку, при авторизации с некорректным паролем')
    def test_login_incorrect_password(self,get_courier):
        courier = Courier([get_courier[0], '322fdX2fa', get_courier[2]])
        response = courier.login()
        assert Response_message.wrong_cred in response.text and response.status_code == 404


    @allure.title('Возвращает ошибку, при авторизации с некорректным логином')
    def test_login_incorrect_login(self, get_courier):
        courier = Courier(['qSwdqw122', get_courier[1], get_courier[2]])
        response = courier.login()
        assert Response_message.wrong_cred in response.text and response.status_code == 404


    @allure.title('Возвращает ошибку, при авторизации несуществующего пользователя')
    def test_login_random_data(self):
        courier = Courier([Helper.generate_random_string(6), Helper.generate_random_string(5), Helper.generate_random_string(4)])
        response = courier.login()
        assert Response_message.wrong_cred in response.text and response.status_code == 404
