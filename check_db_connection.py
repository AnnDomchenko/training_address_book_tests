from db_api.addressbook_db import AddressbookDB

config = {
    "host": "localhost",
    "port": 8889,
    "user": "root",
    "password": "root",
    "db": "test"
}

db = AddressbookDB(**config)

try:
    for c in db.get_contact_list():
        print(c)
finally:
    db.destroy()
