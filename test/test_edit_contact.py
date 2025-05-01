from model.editContact import EditContact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(EditContact(firstName="Updated Anna", phone_mobile="updated 1111",title="updated title", bmonth="May"))
    app.session.logout()