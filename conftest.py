import pytest

from apios.user import User
from apios.announce import Announce

@pytest.fixture()
def user():

    user = User()
    user.sign_up()
    yield user

@pytest.fixture(scope='class')
def announce():

    user = User()
    user.sign_up()
    announce = Announce()
    headers = user.headers
    announce.create_announce(headers)
    yield user, announce