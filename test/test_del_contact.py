from model.contact import Contact
def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="Delete", company="Delete"))
    app.contact.delete_first_contact()