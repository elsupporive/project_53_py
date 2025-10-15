import random
from time import sleep
from model.group import Group
from model.contact import Contact


# ЕСЛИ У ГРУППЫ ПУСТОЕ НАЗВАНИЕ ПОЧЕМУ-ТО ТЕСТ ПАДАЕТ
def test_delete_contact_from_group(app, orm):
    groups_with_contacts = orm.get_group_ids_with_contacts()
    print(groups_with_contacts)
    if len(groups_with_contacts) == 0:
        if len(orm.get_contact_list()) == 0:
            app.contact.create(Contact(nickname="firstContact_nick", company="firstContact_com"))
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name='firstGroup'))
        contact = random.choice(orm.get_contact_list())
        group = random.choice(orm.get_group_list())
        app.contact.add_contact_to_the_group(contact.id, group.id)
        groups_with_contacts = orm.get_group_ids_with_contacts()
    group = random.choice(groups_with_contacts)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_the_group(group.id, contact.id)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) \
           == sorted(new_contacts_in_group, key=Contact.id_or_max)




