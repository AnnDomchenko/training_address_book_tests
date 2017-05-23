from pony.orm import *
from pymysql.converters import conversions
from models.group import Group
from models.contact import Contact
from datetime import datetime


class AddressbookORM:

    db = Database()

    class GroupORM(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

        def get_model(self):
            return Group(id=self.id, name=self.name, header=self.header, footer=self.footer)

    class ContactORM(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int)
        firstname = Optional(str)
        middlename = Optional(str)
        lastname = Optional(str)
        deprecated = Optional(datetime)

        def get_model(self):
            return Contact(id=self.id, firstname=self.firstname, middlename=self.middlename, lastname=self.lastname)

    def __init__(self, host, port, user, password, db):
        self.db.bind('mysql', host=host, port=port, user=user, password=password, db=db, charset="utf8",
                     conv=conversions)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_group_list(self):
        query = select(g for g in self.GroupORM).order_by(self.GroupORM.name, self.GroupORM.id)
        return [g.get_model() for g in query]

    @db_session
    def get_contact_list(self):
        query = select(c for c in self.ContactORM if c.deprecated is None)
        return [c.get_model() for c in query]
