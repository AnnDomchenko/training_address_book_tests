from selenium import webdriver


class AddressBookAPI:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)

    def open_home_page(self):
        wd = self.wd
        # Open home page
        wd.get("http://localhost:8888/addressbook/")

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
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_group_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()

    def create_group(self, group):
        wd = self.wd
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group
        wd.find_element_by_name("submit").click()

    def delete_group_by_number(self, number):
        wd = self.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        checkboxes[number].click()
        wd.find_element_by_name("delete").click()

    def return_to_group_page(self):
        wd = self.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # Logout
        wd.find_element_by_css_selector('form[name="logout"] > a').click()

    def find_message(self):
        wd = self.wd
        return wd.find_element_by_css_selector("div.msgbox").text

    def destroy(self):
        self.wd.quit()
