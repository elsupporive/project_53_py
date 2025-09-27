# "http://macbook-pro-elvira.local/addressbook/index.php"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.wd.implicitly_wait(2)
        elif browser == 'chrome':
            self.wd = webdriver.Chrome(ChromeDriverManager().install())
            self.wd.implicitly_wait(2)
        elif browser == 'ie':
            self.wd = webdriver.Ie(IEDriverManager().install())
            self.wd.implicitly_wait(2)
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()