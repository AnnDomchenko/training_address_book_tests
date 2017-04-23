from models.group import Group


def test_add_group(app):
    test_group = Group(name="group_name", header="header", footer="footer")
    app.open_group_page()
    app.create_group(test_group)
    # TODO: verify message
    app.return_to_group_page()
    # TODO: Verify group in group list

