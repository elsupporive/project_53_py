# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstName="Anna-Mira", lastName="Petrova", nickname="annapetr", company="First Company Anna", address="Moscow, Nikitskaya 22", phone_home="111",
                        phone_mobile="1111", phone_work="111111", fax="11231", email="anna@gmail.com", email2="anna2@gmail.com", email3="anna3@gmail.com",
                        webpage="myhome.com", title="title", bday="9", bmonth="April", byear="2001", an_day="16", an_month="January", an_year="2009")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
