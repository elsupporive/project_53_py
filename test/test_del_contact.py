from model.contact import Contact
from random import randrange
import pytest
import random

@pytest.mark.parametrize("_", range(1))
def test_del_some_contact(app, _, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(nickname="Delete", company="Delete"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



# @pytest.mark.parametrize("_", range(1))
# def test_del_some_contact(app, _, db, check_ui):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(nickname="Delete", company="Delete"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(index)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) - 1 == len(new_contacts)
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts



