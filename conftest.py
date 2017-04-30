import pytest
import random
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


@pytest.fixture(params=[0, "random", -1], ids=["first", "random in middle", "last"])
def index(request, app):
    if request.param == "random":
        return random.randrange(1, app.group.count()-1)
    return request.param


test_groups = [
    Group(name="group_name", header="header", footer="footer"),
    Group(name="123", header="456", footer="7890")
]


@pytest.fixture(params=test_groups, ids=[repr(g) for g in test_groups])
def test_group(request):
    return request.param
