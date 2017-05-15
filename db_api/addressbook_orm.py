from pony.orm import *


class AddressbookORM:

    db = Database()

    class GroupORM(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    def __init__(self, host, port, user, password, db):
        self.db.bind('mysql', host=host, port=port, user=user, password=password, db=db, charset="utf8")
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_group_list(self):
        query = select(g for g in self.GroupORM)
        return list(query)
