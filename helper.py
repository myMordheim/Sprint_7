import allure
import requests
import random
import string
import json
from const import *


class Helper:
    @staticmethod
    @allure.step('Создание рандомного логина/пароля/имя')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    @allure.step('Создание рандомных кредов')
    def generate_data():
        data = [Helper.generate_random_string(10), Helper.generate_random_string(10), Helper.generate_random_string(10)]
        return data

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(login, password):
        response_post = requests.post(Endpoints.LOGIN, data={
            "login": login,
            "password": password,
        })
        courier_id = response_post.json()['id']
        requests.delete(f'{Endpoints.DELETE}/{courier_id}')

    @staticmethod
    @allure.step('Создание курьера и возвращение его кредов')
    def register_new_courier_and_return_login_password():
        login_pass = []

        login = Helper.generate_random_string(10)
        password = Helper.generate_random_string(10)
        first_name = Helper.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Endpoints.CREATE, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(colour):
        order_data = {
            "firstName": "Гендальф",
            "lastName": "Белый",
            "address": "Валинор",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour
        }

        return requests.post(Endpoints.CREATE_ORDER, data=json.dumps(order_data))
