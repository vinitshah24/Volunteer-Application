""" Run this script before running the application """

import pymysql
import config
import api.users.models as users
import api.events.models as events

connection = pymysql.connect(
    host=config.MYSQL_DATABASE_HOST,
    user=config.MYSQL_DATABASE_USER,
    password=config.MYSQL_DATABASE_PASSWORD,
    db=config.MYSQL_DATABASE_DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

DROP_DB = """DROP DATABASE IF EXISTS `{}`
""".format(config.MYSQL_DATABASE_DB).replace('\n', ' ')
CREATE_DB = """CREATE DATABASE IF NOT EXISTS `{}`
""".format(config.MYSQL_DATABASE_DB).replace('\n', ' ')
DROP_USERS_TABLE = """DROP TABLE IF EXISTS `{}`.`{}`
""".format(config.MYSQL_DATABASE_DB, users.TABLE_NAME).replace('\n', ' ')
DROP_EVENTS_TABLE = """DROP TABLE IF EXISTS `{}`.`{}`
""".format(config.MYSQL_DATABASE_DB, events.TABLE_NAME).replace('\n', ' ')

try:
    with connection.cursor() as cursor:
        cursor.execute(DROP_EVENTS_TABLE)
        cursor.execute(DROP_USERS_TABLE)
        cursor.execute(users.CREATE_TABLE)
        cursor.execute(events.CREATE_TABLE)
        connection.commit()
        print("MySQL setup was successful!")
except pymysql.MySQLError as mysql_error:
    print(mysql_error)
finally:
    cursor.close()
