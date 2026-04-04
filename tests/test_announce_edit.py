import pytest
import allure
import requests

from constants import Url, Announce_Data


class TestAnnounceEdit:

    @allure.title('Успешное редактирование поля названия объявления')
    def test_title(self, announce):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        изменяем название, проверяем код ответа и что название изменилось.
        """
        user, announce = announce
        old = announce.title
        url = f'{Url.EDIT_ANNOUNCE}/{announce.id}'
        announce.set_title()
        edit = requests.patch(url, headers=user.headers, files=announce.payload)
        new = edit.json()["name"]

        assert edit.status_code == 200
        assert old != new

    @pytest.mark.parametrize('new_category', Announce_Data.CATEGORIES[1:])
    @allure.title('Успешное редактирование поля категории объявления')
    def test_category(self, announce, new_category):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        меняем категории, проверяем код ответа и что категория изменилась.
        """
        user, announce = announce
        old = announce.category
        url = f'{Url.EDIT_ANNOUNCE}/{announce.id}'
        announce.set_category(new_category)
        edit = requests.patch(url, headers=user.headers, files=announce.payload)
        new = edit.json()["category"]

        assert edit.status_code == 200
        assert old != new

    @allure.title('Успешное редактирование поля состояния товара')
    def test_condition(self, announce):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        изменяем состояние, проверяем код ответа и что состояние в ответе верное.
        """
        user, announce = announce
        old = announce.condition
        url = f'{Url.EDIT_ANNOUNCE}/{announce.id}'
        announce.set_condition(Announce_Data.COND[1])
        edit = requests.patch(url, headers=user.headers, files=announce.payload)
        new = edit.json()["condition"]

        assert edit.status_code == 200
        assert old != new

    @pytest.mark.parametrize('new_city', Announce_Data.CITIES[1:])
    @allure.title('Успешное редактирование города в объявлении')
    def test_city(self, announce, new_city):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        меняем категории, проверяем код ответа и что категория изменилась.
        """
        user, announce = announce
        old = announce.city
        url = f'{Url.EDIT_ANNOUNCE}/{announce.id}'
        announce.set_city(new_city)
        edit = requests.patch(url, headers=user.headers, files=announce.payload)
        new = edit.json()["city"]

        assert edit.status_code == 200
        assert old != new

    @allure.title('Успешное редактирование поля описания объявления')
    def test_description(self, announce):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        изменяем описание, проверяем код ответа и что описание изменилось.
        """
        user, announce = announce
        old = announce.description
        url = f'{Url.EDIT_ANNOUNCE}/{announce.id}'
        announce.set_description()
        edit = requests.patch(url, headers=user.headers, files=announce.payload)
        new = edit.json()["description"]

        assert edit.status_code == 200
        assert old != new

    @allure.title('Успешное редактирование поля цены в объявлении')
    def test_price(self, announce):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        изменяем описание, проверяем код ответа и что описание изменилось.
        """
        user, announce = announce
        old = announce.price
        url = f'{Url.EDIT_ANNOUNCE}/{announce.id}'
        announce.set_price()
        edit = requests.patch(url, headers=user.headers, files=announce.payload)
        new = edit.json()["price"]

        assert edit.status_code == 200
        assert old != new

    @allure.title('Редактирование объявления не с тем токеном')
    def test_token_wrong(self, announce):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        изменяем токен, проверяем код ответа.
        """
        user, announce = announce      
        url = f'{Url.EDIT_ANNOUNCE}/{announce.id}'
        announce.set_title()
        user.break_token(user.token)
        edit = requests.patch(url, headers=user.headers_bt, files=announce.payload)

        assert edit.status_code == 401
        assert edit.json()['messege'] == "Токен не действителен"

