import pytest
from web_api.addressbook_api import AddressBookAPI


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
