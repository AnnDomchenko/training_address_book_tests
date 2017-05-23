import pytest


def test_add_group(app, init_login, test_group, db):
    with pytest.allure.step("GIVEN a group list"):
        old_groups_list = db.get_group_list()
    with pytest.allure.step("WHEN I add the group {}".format(test_group)):
        app.group.open_group_page()
        app.group.create(test_group)
    with pytest.allure.step("THEN the success message appears"):
        assert "A new group has been entered into the address book." in app.find_message()
    app.group.return_to_group_page()
    with pytest.allure.step("THEN the new group list is equal to the old list with new added group"):
        new_groups_list = db.get_group_list()
        assert len(old_groups_list) + 1 == len(new_groups_list)
        old_groups_list.append(test_group)
        assert sorted(old_groups_list) == sorted(new_groups_list)
