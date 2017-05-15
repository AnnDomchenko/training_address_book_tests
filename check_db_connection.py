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
    for g in db.get_group_list():
        print(g)
finally:
    pass
