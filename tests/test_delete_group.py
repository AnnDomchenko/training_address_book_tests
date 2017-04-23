import pytest
from models.group import Group


@pytest.fixture
def init_group(app, init_login):
    if not app.is_group_present():
        test_group = Group(name="test name")
        app.create_group(test_group)


def test_delete_group(app, init_login, init_group):
    app.open_group_page()
    app.delete_group_by_number(0)
    assert "Group has been removed." in app.find_message()
    app.return_to_group_page()
    # TODO: Deletion group in list
