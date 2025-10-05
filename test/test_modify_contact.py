from model.contact import Contact
from random import randrange
import random

def test_modify_contact(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstName="new", nickname="new"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    update_contact = Contact(firstName="Updated8", lastName="Petrov", bmonth = "May")
    update_contact.id = contact.id
    app.contact.modify_contact_by_id(update_contact.id, update_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = update_contact
    assert sorted(old_contacts, key=Contact.id_or_max) \
           == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



# def test_modify_contact(app, db, check_ui):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstName="new", nickname="new"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(firstName="Updated8", lastName="Petrov", bmonth = "May")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
