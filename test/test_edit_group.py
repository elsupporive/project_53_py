def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(name="Updated group")
    app.session.logout()