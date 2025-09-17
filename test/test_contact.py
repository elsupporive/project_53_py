from random import randrange


def test_contact_on_home_page(app):
    contact = app.contact.get_contact_list()
    index = randrange(len(contact))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastName == contact_from_edit_page.lastName
    assert contact_from_home_page.firstName == contact_from_edit_page.firstName
    assert contact_from_home_page.address == contact_from_edit_page.address
    merged_phones = app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merged_phones
    merged_emails = app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    print(merged_emails)
    assert contact_from_home_page.all_emails_from_home_page == merged_emails


