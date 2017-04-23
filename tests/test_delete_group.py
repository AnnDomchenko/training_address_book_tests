def test_delete_group(app):
    app.open_group_page()
    app.delete_group_by_number(0)
    assert "Group has been removed." in app.find_message()
    app.return_to_group_page()
    # TODO: Deletion group in list
