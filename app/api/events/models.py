""" Events Model """

from config import MYSQL_DATABASE_DB
from api.users.models import TABLE_NAME as USERS_TABLE

TABLE_NAME = "events"

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS {database}.{table} (
id INT AUTO_INCREMENT PRIMARY KEY,
public_id VARCHAR(60) NOT NULL UNIQUE,
name VARCHAR(50) NOT NULL,
category VARCHAR(50) NOT NULL,
details VARCHAR(10000) NOT NULL,
address VARCHAR(50) NOT NULL,
county VARCHAR(50) NOT NULL,
state VARCHAR(100) NOT NULL,
date DATE NOT NULL,
time TIME NOT NULL,
user_public_id VARCHAR(60) NOT NULL,
CONSTRAINT fk_user_public_id FOREIGN KEY (user_public_id)
REFERENCES volunteer_db.users (public_id)
)
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME).replace('\n', ' ')

SELECT_EVENTS = """SELECT {events_table}.*,
{users_table}.username, {users_table}.first_name, {users_table}.last_name
FROM {database}.{events_table}
LEFT JOIN {database}.{users_table}
ON {events_table}.user_public_id = {users_table}.public_id
""".format(database=MYSQL_DATABASE_DB,
           events_table=TABLE_NAME,
           users_table=USERS_TABLE).replace('\n', ' ')

INSERT_EVENT = """INSERT INTO {database}.{events_table}
(public_id, name, category, details, address, county, state, date, time, user_public_id )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
""".format(database=MYSQL_DATABASE_DB, events_table=TABLE_NAME).replace('\n', ' ')

DELETE_EVENT = """DELETE FROM {database}.{events_table}
WHERE {events_table}.public_id = %s and {events_table}.user_public_id = %s
""".format(database=MYSQL_DATABASE_DB, events_table=TABLE_NAME).replace('\n', ' ')
