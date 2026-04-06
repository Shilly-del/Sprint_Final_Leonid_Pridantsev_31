import pytest
import allure
import requests

from apios.announce import Announce
from constants import Url, AnnounceData


class TestAnnounceCreate:

    @pytest.mark.parametrize('category', AnnounceData.CATEGORIES)
    @allure.title('Успешное создание объявления в любой категории')
    def test_create(self, user, category):
        """
        С помощью фикстуры регистрируем пользователя создаём объявление,
        проверяем код ответа.
        """
        announce = Announce()
        announce.set_category(category)
        headers = user.headers
        r = requests.post(Url.CREATE_ANNOUNCE, headers=headers, files=announce.payload)
        data = r.json()

        assert r.status_code == 201
        assert announce.title ==  data['name']
        assert announce.category == data['category']
        assert announce.condition == data['condition']
        assert announce.city == data['city']
        assert announce.description == data['description']
        assert announce.price == data['price']

