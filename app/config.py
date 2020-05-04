""" Configuration Variables """
import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = os.getenv('DEBUG')
PORT = 5000
HOST = os.getenv('HOST')

SECRET_KEY = os.getenv('SECRET_KEY')

MYSQL_DATABASE_HOST = os.getenv('MYSQL_DATABASE_HOST')
MYSQL_DATABASE_PORT = 3306
MYSQL_DATABASE_USER = os.getenv('MYSQL_DATABASE_USER')
MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_DATABASE_PASSWORD')
MYSQL_DATABASE_DB = os.getenv('MYSQL_DATABASE_DB')

PROPAGATE_EXCEPTIONS = True
JWT_BLACKLIST_ENABLED = True  # enable blacklist feature
# allow blacklisting for access and refresh tokens
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
