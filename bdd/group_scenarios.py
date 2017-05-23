import random
from pytest_bdd import given, then, when, scenario
from models.group import Group


@scenario("group.feature", "Add new group")
def test_add_new_group():
    pass


@scenario("group.feature", "Delete a random group")
def test_delete_group():
    pass


@given("a group list")
def old_groups_list(db):
    return db.get_group_list()


@given("a group with <name>, <header>, <footer>")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when("I add this new group to the list")
def add_new_group(app, init_login, new_group):
    app.group.open_group_page()
    app.group.create(new_group)
    app.group.return_to_group_page()


@then("a new group list is equal to the old list with the new group")
def verify_group_adding(db, old_groups_list, new_group):
    new_groups_list = db.get_group_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(new_group)
    assert sorted(old_groups_list) == sorted(new_groups_list)


@given("a non-empty group list")
def non_empty_group_list(init_group, db):
    return db.get_group_list()


@given("a random group")
def random_group_index(app, init_login):
    return random.randrange(app.group.count())


@when("I delete the group")
def delete_group(app, random_group_index):
    app.group.open_group_page()
    app.group.delete_by_number(random_group_index)
    app.group.return_to_group_page()


@then("the new group list is equal to the old list without the deleted group")
def verify_group_deleting(db, random_group_index, non_empty_group_list):
    old_groups_list = non_empty_group_list
    new_groups_list = db.get_group_list()
    assert len(old_groups_list) - 1 == len(new_groups_list)
    old_groups_list.pop(random_group_index)
    assert old_groups_list == new_groups_list
