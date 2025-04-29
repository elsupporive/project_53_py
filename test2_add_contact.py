from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from model.contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)


    def open_home_page(self, driver):
        driver.get("http://macbook-pro-elvira.local/addressbook/edit.php")

    def login(self, driver, username, password):
        self.open_home_page(driver)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, driver, contact):
        # fill new contact info
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstName)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastName)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.phone_home)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.phone_work)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email3)
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(contact.webpage)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("theform").click()
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        driver.find_element_by_xpath("//option[@value='9']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_xpath("//option[@value='April']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_name("theform").click()
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.an_day)
        driver.find_element_by_xpath("//div[@id='content']/form/select[3]/option[18]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.an_month)
        driver.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(contact.an_year)
        driver.find_element_by_name("theform").click()
        # submit new contact
        driver.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page(driver)

    def return_to_home_page(self, driver):
        driver.find_element_by_link_text("home").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_contact(driver, Contact(firstName="Anna", lastName="Petrova", nickname="annapetr", company="First Company Anna", address="Moscow, Nikitskaya 22", phone_home="111",
                            phone_mobile="1111", phone_work="111111", fax="11231", email="anna@gmail.com", email2="anna2@gmail.com", email3="anna3@gmail.com",
                            webpage="myhome.com", title="title", bday="9", bmonth="April", byear="2001", an_day="16", an_month="January", an_year="2009"))
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
