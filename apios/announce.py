import allure
import random
import requests

from constants import Url, Announce_Data
from helpers.data_gen import generate_random_string

class Announce:
    @allure.step('Создание данных объявления')
    def __init__(self):
        self.title = generate_random_string(7)
        self.category = Announce_Data.CATEGORIES[0]
        self.condition = Announce_Data.COND[0]
        self.city = Announce_Data.CITIES[0]
        self.description = generate_random_string(10)
        self.price = random.randint(1000, 10000)
        self.payload = {
                'name': (None, self.title),
                'category': (None, self.category),
                'condition': (None, self.condition),
                'city': (None, self.city),
                'description': (None, self.description),
                'price': (None, str(self.price))
            }

    @allure.step('Регистрация объявления')
    def create_announce(self, headers):
        r = requests.post(Url.CREATE_ANNOUNCE, headers=headers, files=self.payload)
        self.id = r.json()["id"]

    @allure.step('Устанавливаем наименование объявления')
    def set_title(self):
        self.title = generate_random_string(7)
        self.payload['name'] = (None, self.title)

    @allure.step('Устанавливаем категорию объявления')
    def set_category(self, category):
        self.category = category
        self.payload['category'] = (None, self.category)

    @allure.step('Устанавливаем состояние')
    def set_condition(self, condition):
        self.condition = condition
        self.payload['condition'] = (None, self.condition)

    @allure.step('Устанавливаем город')
    def set_city(self, city):
        self.city = city
        self.payload['city'] = (None, self.city)

    @allure.step('Устанавливаем описание')
    def set_description(self):
        self.description = generate_random_string(10)
        self.payload['description'] = (None, self.description)

    @allure.step('Устанавливаем цену')
    def set_price(self):
        self.price = random.randint(1000, 10000)
        self.payload['price'] = (None, self.price)