import pytest
from web_api.addressbook_api import AddressBookAPI
from models.group import Group


@pytest.fixture(scope="session")
def app():
    addr_api = AddressBookAPI()
    yield addr_api
    addr_api.destroy()


@pytest.fixture(scope="session")
def init_login(app):
    app.session.login(username="admin", password="secret")
    yield
    app.session.logout()


@pytest.fixture
def init_group(app, init_login):
    if not app.group.is_present():
        test_group = Group(name="test name")
        app.group.create(test_group)
