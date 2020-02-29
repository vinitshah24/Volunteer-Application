""" Users-Events Relationship Model """

from config import MYSQL_DATABASE_DB
from api.users.models import TABLE_NAME as USERS_TABLE
from api.events.models import TABLE_NAME as EVENTS_TABLE

TABLE_NAME = "rsvp"

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS {database}.{table} (
CREATE TABLE IF NOT EXISTS volunteer_db.rsvp (
id INT AUTO_INCREMENT PRIMARY KEY,
user_public_id VARCHAR(60) NOT NULL,
event_public_id VARCHAR(60) NOT NULL UNIQUE,
CONSTRAINT fk_rsvp_user_public_id FOREIGN KEY (user_public_id) REFERENCES volunteer_db.users (public_id),
CONSTRAINT fk_rsvp_event_public_id FOREIGN KEY (event_public_id) REFERENCES volunteer_db.events (public_id)
)
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME, ).replace('\n', ' ')

INSERT_RSVP = """INSERT INTO {database}.{table}
(user_public_id, event_public_id) VALUES (%s, %s)
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME, ).replace('\n', ' ')

CHECK_RECORD = """SELECT COUNT(*) > 0 AS record_count
FROM {database}.{table} WHERE user_public_id = %s AND event_public_id = %s
""".format(database=MYSQL_DATABASE_DB, table=TABLE_NAME, ).replace('\n', ' ')

SELECT_USER_RSVP = """SELECT {events_table}.*
FROM {database}.{rsvp_table}
INNER JOIN {database}.{users_table}
ON {rsvp_table}.user_public_id = {users_table}.public_id
INNER JOIN {database}.{events_table}
ON {rsvp_table}.event_public_id = {events_table}.public_id
WHERE {rsvp_table}.user_public_id = %s
""".format(database=MYSQL_DATABASE_DB,
           rsvp_table=TABLE_NAME,
           users_table=USERS_TABLE,
           events_table=EVENTS_TABLE).replace('\n', ' ')
