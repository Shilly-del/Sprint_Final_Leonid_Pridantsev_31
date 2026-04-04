import pytest
import allure
import requests

from apios.announce import Announce
from constants import Url, Announce_Data


class TestAnnounceCreate:

    @pytest.mark.parametrize('category', Announce_Data.CATEGORIES)
    @allure.title('Успешное создание объявления в любой категории')
    def test_create(self, user, category):
        """
        С помощью фикстуры регистрируем пользователя создаём объявление,
        проверяем код ответа.
        """
        announce = Announce()
        announce.set_category(category)
        headers = user.headers
        anr = requests.post(Url.CREATE_ANNOUNCE, headers=headers, files=announce.payload)

        assert anr.status_code == 201

