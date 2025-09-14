from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill new contact info
        self.change_cnt_field_value("firstname", contact.firstName)
        self.change_cnt_field_value("lastname", contact.lastName)
        self.change_cnt_field_value("nickname", contact.nickname)
        self.change_cnt_field_value("company", contact.company)
        self.change_cnt_field_value("address", contact.address)
        self.change_cnt_field_value("home", contact.phone_home)
        self.change_cnt_field_value("mobile", contact.phone_mobile)
        self.change_cnt_field_value("work", contact.phone_work)
        self.change_cnt_field_value("fax", contact.fax)
        self.change_cnt_field_value("email", contact.email)
        self.change_cnt_field_value("email2", contact.email2)
        self.change_cnt_field_value("email3", contact.email3)
        self.change_cnt_field_value("homepage", contact.webpage)
        self.change_cnt_field_value("title", contact.title)
        self.change_date_field_value("bday", contact.bday)
        self.change_date_field_value("bmonth", contact.bmonth)
        self.change_cnt_field_value("byear", contact.byear)
        self.change_date_field_value("aday", contact.an_day)
        self.change_date_field_value("amonth", contact.an_month)
        self.change_cnt_field_value("ayear", contact.an_year)


    def change_date_field_value(self, field_date, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element_by_name(field_date).click()
            Select(wd.find_element_by_name(field_date)).select_by_visible_text(date)

    def change_cnt_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, updated_contact):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, updated_contact):
        wd = self.app.wd
        self.return_to_home_page()
        # open modification form
        row = wd.find_elements_by_css_selector("tr[name='entry']")[index]
        row.find_element_by_css_selector("img[title='Edit']").click()
        self.fill_contact_form(updated_contact)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if "Last name" not in wd.page_source and "First name" not in wd.page_source:
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                el = element.find_elements_by_tag_name("td")
                last_name = el[1].text
                first_name = el[2].text
                self.contact_cache.append(Contact(id=id, lastName=last_name, firstName=first_name))
        return list(self.contact_cache)







