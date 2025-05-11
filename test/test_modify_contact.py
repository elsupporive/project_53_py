from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="new", nickname="new"))
    app.contact.modify_first_contact(Contact(firstName="Updated", bmonth = "May"))
