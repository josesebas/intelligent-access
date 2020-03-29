#from pymongo import MongoClient
from flask_mysqldb import MySQL
from config.config import db as config

class DB:
    def __init__(self, app):
        app.config['MYSQL_HOST'] = config['host']
        app.config['MYSQL_USER'] = config['user']
        app.config['MYSQL_PASSWORD'] = config['password']
        app.config['MYSQL_DB'] = config['name']
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
        self.mysql = MySQL(app)
