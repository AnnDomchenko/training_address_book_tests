import pymysql

config = {
    "host": "localhost",
    "port": 8889,
    "user": "root",
    "password": "root",
    "db": "test",
    "charset": "utf8"
}

connection = pymysql.connect(**config)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM group_list;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    connection.close()
