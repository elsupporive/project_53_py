import pymysql.cursors
from fixture.db import DbFixture

db = DbFixture(
    host="127.0.0.1",
    user="root",
    password="",
    name="addressbook"
)
try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
