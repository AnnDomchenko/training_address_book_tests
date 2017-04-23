import unittest
from models.group import Group
from web_api.addressbook_api import AddressBookAPI


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = AddressBookAPI()
    
    def test_test_add_group(self):
        test_group = Group(name="group_name", header="header", footer="footer")
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_group_page()
        self.app.create_group(test_group)
        self.app.return_to_group_page()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
