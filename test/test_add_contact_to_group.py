import random
from time import sleep
from model.group import Group
from model.contact import Contact


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(nickname="firstContact_nick", company="firstContact_com"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name='firstGroup'))
    groups = orm.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    while contact in old_contacts_in_group:
        contact = random.choice(contacts)
    app.contact.add_contact_to_the_group(contact.id, group.id)
    old_contacts_in_group.append(contact)
    new_groups = orm.get_contacts_in_group(Group(id=group.id))
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_groups, key=Contact.id_or_max)

