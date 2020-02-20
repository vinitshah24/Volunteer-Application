""" Users Model """

from config import MYSQL_DATABASE_DB

TABLE_NAME = "users"

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS {database}.{table} (
id INT AUTO_INCREMENT PRIMARY KEY,
public_id VARCHAR(60) NOT NULL UNIQUE,
first_name VARCHAR(80) NOT NULL,
last_name VARCHAR(80) NOT NULL,
email VARCHAR(80) NOT NULL,
username VARCHAR(80) NOT NULL,
password VARCHAR(80) NOT NULL,
is_admin BOOLEAN
)
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

INSERT_TABLE = """INSERT INTO {database}.{table} (
public_id, first_name, last_name, email, username, password, is_admin) 
VALUES(%s, %s, %s, %s, %s, %s, %s)
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

SELECT_ALL = """SELECT * FROM {database}.{table}
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

SELECT_BY_USERNAME_PASS = """SELECT * FROM {database}.{table} 
WHERE username = %s AND password = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

SELECT_BY_PUBLIC_ID = """SELECT * FROM {database}.{table} 
WHERE public_id = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

UPDATE_NAME = """UPDATE {database}.{table}
SET first_name = %s, last_name = %s WHERE public_id = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

UPDATE_EMAIL = """UPDATE {database}.{table}
SET email = %s WHERE public_id = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

UPDATE_PASSWORD = """UPDATE {database}.{table}
SET password = %s WHERE public_id = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

UPDATE_ADMIN_STATUS = """UPDATE {database}.{table} SET is_admin = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

DELETE_BY_PUBLIC_ID = """DELETE FROM {database}.{table} 
WHERE public_id = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

SELECT_BY_USERNAME = """SELECT * FROM {database}.{table} 
WHERE username = %s LIMIT 1
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

SELECT_BY_EMAIL = """SELECT * FROM {database}.{table} 
WHERE email = %s LIMIT 1
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')
