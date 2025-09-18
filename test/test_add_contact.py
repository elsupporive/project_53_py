# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    return "+79" + "".join([random.choice(string.digits) for i in range(maxlen)])

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

testdata = [Contact(firstName="firstName3", lastName=random_string("lastName", 10),
                    nickname=random_string("nickname", 10), company=random_string("company", 10),
                    address=random_string("nickname", 20),
                    phone_home=random_numbers(9), phone_mobile=random_numbers(9), phone_work=random_numbers(9), fax=random_numbers(9),
                    email=random_email(10)+"@gmail.com", email2=random_email(10)+"@gmail.com", email3=random_email(10)+"@gmail.com",
                    webpage=random_string("web", 5) + ".com", title=random_string("nickname", 5),
                    bday=str(random.randint(1, 31)), bmonth=str(random.choice(months)), byear=str(random.randint(1900, 2025)),
                    an_day=str(random.randint(1, 31)), an_month=str(random.choice(months)), an_year=str(random.randint(1900, 2025)))
            for i in range(2)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
