import allure
import pytest
import requests

from constants import Url


class TestSignIn:

    @allure.title('Проверка успешной авторизации пользователя')
    @pytest.mark.xfail(reason='Код ответа 201.')
    def test_signin_succesfull(self, user):
        """
        С помощью фикстуры регистрируем пользователя, после чего авторизуемся.
        Авторизация работает, но возвращается код 201, как правило используемый
        для создания новых объектов. В данном случае более подходит код 200.
        """
        
        reg = requests.post(Url.SIGNIN, data=user.payload)

        assert reg.status_code == 200

