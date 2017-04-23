import pytest
from models.group import Group
from web_api.addressbook_api import AddressBookAPI


@pytest.fixture
def app():
    addr_api = AddressBookAPI()
    addr_api.login(username="admin", password="secret")
    yield addr_api
    addr_api.logout()
    addr_api.destroy()


def test_add_group(app):
    test_group = Group(name="group_name", header="header", footer="footer")
    app.open_group_page()
    app.create_group(test_group)
    # TODO: verify message
    app.return_to_group_page()
    # TODO: Verify group in group list

