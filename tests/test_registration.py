import allure
import requests

from constants import Url
from apios.user import User


class TestRegistration:

    @allure.title('Проверка успешной регистрации пользователя')
    def test_register_succesfull(self):
        """
        Создаём данные пользователя, отправляем запрос на регистрацию.
        """
        user = User()
        reg = requests.post(Url.SIGNUP, data=user.payload)

        assert reg.status_code == 201

    @allure.title('Проверка повторной регистрации пользователя')
    def test_register_repeat(self):
        """
        Отправляем запрос на регистрацию с данными уже зарегисрированного
        пользователя
        """
        user = User()
        reg = requests.post(Url.SIGNUP, data=user.payload)
        reg = requests.post(Url.SIGNUP, data=user.payload)

        assert reg.status_code == 400
        assert reg.json()["message"] == "Почта уже используется"

