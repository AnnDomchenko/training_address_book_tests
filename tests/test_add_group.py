from models.group import Group


def test_add_group(app, init_login):
    test_group = Group(name="group_name", header="header", footer="footer")
    app.open_group_page()
    app.create_group(test_group)
    assert "A new group has been entered into the address book." in app.find_message()
    app.return_to_group_page()
    # TODO: Verify group in group list

