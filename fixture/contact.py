from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
from time import sleep

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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()

    def add_contact_to_the_group(self, id, group_id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath(f"//select[@name='to_group']/option[@value='{group_id}']").click()
        sleep(3)
        wd.find_element_by_name('add').click()
        sleep(3)

    def delete_contact_from_the_group(self, group_id, id):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_xpath(f"//select[@name='group']/option[@value='{group_id}']").click()
        sleep(3)
        self.select_contact_by_id(id)
        sleep(3)
        wd.find_element_by_name('remove').click()
        sleep(3)



    def modify_contact_by_id(self, id, updated_contact):
        wd = self.app.wd
        self.return_to_home_page()
        # open modification form
        row = wd.find_element_by_xpath(f"//a[contains(@href, 'id={id}')]/ancestor::tr")
        row.find_element_by_css_selector("img[title='Edit']").click()
        self.fill_contact_form(updated_contact)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

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

    def delete_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_id(contact_id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id=id, lastName=last_name, firstName=first_name,
                                                  address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def view_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        phone_home = wd.find_element_by_name('home').get_attribute('value')
        phone_mobile = wd.find_element_by_name('mobile').get_attribute('value')
        phone_work = wd.find_element_by_name('work').get_attribute('value')
        return Contact(firstName=firstname, lastName=lastname, id=id,
                       phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work,
                       email=email, email2=email2, email3=email3,
                       address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.view_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        print("DEBUG:", text)
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        return Contact(phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                                               [contact.phone_home, contact.phone_mobile,
                                                                contact.phone_work]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3])))



















