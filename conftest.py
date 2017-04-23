import pytest
from web_api.addressbook_api import AddressBookAPI


@pytest.fixture(scope="session")
def app():
    addr_api = AddressBookAPI()
    addr_api.login(username="admin", password="secret")
    yield addr_api
    addr_api.logout()
    addr_api.destroy()