from flask_mysqldb import MySQL

from flask import Flask
from itsdangerous import URLSafeTimedSerializer

from config import Configuration


PROD_HOST = 'localhost'
PROD_PORT = '3306'
PROD_USER = 'asdf'
PROD_PASS = 'asdf@'
PROD_DB_NAME = 'TestDB'


app = Flask(__name__)
app.config.from_object(Configuration)

# app.config['MYSQL_HOST'] = PROD_HOST
# app.config['MYSQL_PORT'] = int(PROD_PORT)
# app.config['MYSQL_DB'] = PROD_DB_NAME
# app.config['MYSQL_USER'] = PROD_USER
# app.config['MYSQL_PASSWORD'] = PROD_PASS
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# mysql = MySQL(app)

# if mysql:
#     print('---------------------------------------------------------')
#     print('  ----  Connected to TestDB!')
#     print('---------------------------------------------------------')
# else:
#     print('---------------------------------------------------------')
#     print('  ----  Conection Error!')
#     print('---------------------------------------------------------')

expiration = 300 #1800 #900s=15min // 600s=10min // 300s=5min
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"], expiration)