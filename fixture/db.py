import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password="", autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3"
                           " from addressbook where deprecated is NULL"
                        )
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(id=str(id), firstName=firstname, lastName=lastname, address=address,
                                    phone_home=home, phone_work=work, phone_mobile=mobile, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def merged_phones_from_db(self, contact):
        return "\n".join([contact.phone_home, contact.phone_mobile, contact.phone_work])

    def merged_emails_from_db(self, contact):
        return "\n".join([contact.email, contact.email2, contact.email3])


    def destroy(self):
        self.connection.close()