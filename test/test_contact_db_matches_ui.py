from model.contact import Contact

def test_contact_on_the_main_page_ui_db(app, db):
    contacts_ui = app.contact.get_contact_list()
    contacts_db = db.get_contact_list()
    sorted_ui = sorted(contacts_ui, key=Contact.id_or_max)
    sorted_db = sorted(contacts_db, key=Contact.id_or_max)
    for i in range(len(sorted_ui)):
        assert sorted_ui[i].lastName == sorted_db[i].lastName
        assert sorted_ui[i].firstName == sorted_db[i].firstName
        assert sorted_ui[i].address == sorted_db[i].address
        merged_phones_db = db.merged_phones_from_db(sorted_db[i])
        assert merged_phones_db == sorted_ui[i].all_phones_from_home_page
        merged_emails_db = db.merged_emails_from_db(sorted_db[i])
        assert merged_emails_db == sorted_ui[i].all_emails_from_home_page






