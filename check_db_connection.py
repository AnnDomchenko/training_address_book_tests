from db_api.addressbook_orm import AddressbookORM

config = {
    "host": "localhost",
    "port": 8889,
    "user": "root",
    "password": "root",
    "db": "test"
}

db = AddressbookORM(**config)

try:
    l = db.get_contact_list()
    for c in l:
        print(c)
    print(len(l))
finally:
    pass
