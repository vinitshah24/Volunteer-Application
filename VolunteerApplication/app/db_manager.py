""" Run this script before running the application """

import pymysql
import config
from api.users.models import CREATE_TABLE

connection = pymysql.connect(
    host=config.MYSQL_DATABASE_HOST,
    user=config.MYSQL_DATABASE_USER,
    password=config.MYSQL_DATABASE_PASSWORD,
    db=config.MYSQL_DATABASE_DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

DROP_DB = "DROP DATABASE IF EXISTS {}".format(config.MYSQL_DATABASE_DB)
CREATE_DB = "CREATE DATABASE IF NOT EXISTS {}".format(config.MYSQL_DATABASE_DB)

try:
    with connection.cursor() as cursor:
        cursor.execute(DROP_DB)
        cursor.execute(CREATE_DB)
        cursor.execute(CREATE_TABLE)
        connection.commit()
        print("Success!")
except pymysql.MySQLError as e:
    print(e)
finally:
    cursor.close()
