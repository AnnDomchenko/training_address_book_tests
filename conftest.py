import pytest
import random
import json
import os.path
from web_api.addressbook_api import AddressBookAPI
from models.group import Group
from data.test_groups import test_groups


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")


@pytest.fixture(scope="session")
def config(request):
    file_name = request.config.getoption("--config")
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def app(request, config):
    browser = request.config.getoption("--browser")
    addr_api = AddressBookAPI(browser=browser, base_url=config["base_url"])
    yield addr_api
    addr_api.destroy()


@pytest.fixture(scope="session")
def init_login(app, config):
    app.session.login(username=config["username"], password=config["password"])
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


@pytest.fixture(params=test_groups, ids=[repr(g) for g in test_groups])
def test_group(request):
    return request.param
