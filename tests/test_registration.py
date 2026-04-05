import allure
import requests

from constants import Url, ApiMessage
from apios.user import User


class TestRegistration:

    @allure.title('Проверка успешной регистрации пользователя')
    def test_register_succesfull(self):
        """
        Создаём данные пользователя, отправляем запрос на регистрацию.
        Проверяем, что в ответе email пользователя совпадает с отправленным.
        """
        user = User()

        reg = requests.post(Url.SIGNUP, data=user.payload)

        assert reg.status_code == 201
        assert reg.json()['user']["email"] == user.email


    @allure.title('Проверка повторной регистрации пользователя')
    def test_register_repeat(self):
        """
        Отправляем запрос на регистрацию с данными уже зарегисрированного
        пользователя. Проверяем код и сообщение ответа.
        """
        user = User()
        reg = requests.post(Url.SIGNUP, data=user.payload)
        reg = requests.post(Url.SIGNUP, data=user.payload)

        assert reg.status_code == 400
        assert reg.json()["message"] == ApiMessage.REMAIL

