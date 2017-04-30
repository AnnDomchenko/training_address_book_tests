from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of, element_to_be_clickable


class SessionHelper:
    def __init__(self):
        pass

    def login(self, username, password):
        self.open_home_page()
        wd = self.wd
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        button = wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]")
        button.click()
        WebDriverWait(wd, 15).until(staleness_of(button))

    def logout(self):
        wd = self.wd
        # Finding link with waiting when it will be clickable
        link = WebDriverWait(wd, 15).until(element_to_be_clickable((By.CSS_SELECTOR, 'form[name="logout"] > a')))
        link.click()
