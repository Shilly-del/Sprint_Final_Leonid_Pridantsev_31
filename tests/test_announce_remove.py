import allure
import requests

from constants import Url, ApiMessage


class TestAnnounceRemove:

    @allure.title('Успешное удаление объявления')
    def test_remove(self, announce):
        """
        С помощью фикстуры регистрируем пользователя, создаём объявление,
        удаляем, проверяем код ответа и сообщение об удалении.
        """
        user, announce = announce
        url = f'{Url.REMOVE_ANNOUNCE}/{announce.id}'
        r = requests.delete(url, headers=user.headers, files=announce.payload)

        assert r.status_code == 200
        assert r.json()['message'] == ApiMessage.ANNONCEREM
