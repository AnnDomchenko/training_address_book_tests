import pytest
from models.group import Group
from web_api.addressbook_api import AddressBookAPI


@pytest.fixture
def app():
    addr_api = AddressBookAPI()
    yield addr_api
    addr_api.destroy()


def test_add_group(app):
    test_group = Group(name="group_name", header="header", footer="footer")
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(test_group)
    app.return_to_group_page()
    app.logout()
