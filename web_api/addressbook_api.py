from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from web_api.session_helper import SessionHelper
from web_api.group_helper import GroupHelper
from web_api.contact_helper import ContactHelper


class AddressBookAPI:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper()
        self.group = GroupHelper()
        self.contact = ContactHelper()

    def open_home_page(self):
        wd = self.wd
        # Open home page
        wd.get("http://localhost:8888/addressbook/")

    def is_element_present(self, by, locator):
        wd = self.wd
        try:
            wd.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    def find_message(self):
        wd = self.wd
        return wd.find_element_by_css_selector("div.msgbox").text

    def destroy(self):
        self.wd.quit()
