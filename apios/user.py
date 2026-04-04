import allure
import requests

from constants import Url
from helpers.data_gen import create_email, generate_random_string

class User:
    @allure.step('Создание данных пользователя')
    def __init__(self):
        self.email = create_email()
        self.password = generate_random_string(10)
        self.payload = {
            "email": self.email,
            "password": self.password
        }

    @allure.step('Регистрация пользователя')
    def sign_up(self):
        r = requests.post(Url.SIGNUP, data=self.payload)
        self.token = r.json()['access_token']['access_token']
        self.headers = {'Authorization': f'Bearer {self.token}'}

    @allure.step('Ломаем токен')
    def break_token(self, token):
        s = chr((ord(self.token[-1]) + 1 - 32) % 95 + 32)
        token = self.token[:-1] + s
        self.headers_bt = {'Authorization': f'Bearer {token}'}
