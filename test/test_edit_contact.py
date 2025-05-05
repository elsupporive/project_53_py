from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstName="Updated Anna", lastName="Updated Petrova", nickname="Updated annapetr", company="Updated First Company Anna", address="Updated Moscow, Nikitskaya 22", phone_home="Updated 111",
                        phone_mobile="Updated 1111", phone_work="Updated 111111", fax="Updated 11231", email="up_anna@gmail.com", email2="up_anna2@gmail.com", email3="up_anna3@gmail.com",
                        webpage="up_myhome.com", title="Updated title", bday="9", bmonth="May", byear="2001", an_day="16", an_month="May", an_year="2009"))
    app.session.logout()