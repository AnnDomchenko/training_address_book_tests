import pytest
from models.group import Group


@pytest.fixture
def init_group(app, init_login):
    if not app.group.is_present():
        test_group = Group(name="test name")
        app.group.create(test_group)


def test_delete_group(app, init_login, init_group):
    app.group.open_group_page()
    old_groups_list = app.group.get_list()
    app.group.delete_by_number(0)
    assert "Group has been removed." in app.find_message()
    app.group.return_to_group_page()
    # Verifying Deletion group in list
    new_groups_list = app.group.get_list()
    assert len(old_groups_list)-1 == len(new_groups_list)
    old_groups_list.pop(0)
    assert old_groups_list == new_groups_list
