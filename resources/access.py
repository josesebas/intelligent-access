from flask_restful import Resource, request
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
#from libs.mysql import DB
from bson.json_util import dumps, loads, default

class Access(Resource):
    def __init__(self, **kwargs):
        self.log = Logger()
        self.conn = kwargs['conn']
    def get(self):
        cur = self.conn.mysql.connection.cursor()
        cur.execute("SELECT * FROM access WHERE id = 1")
        self.conn.mysql.connection.commit()
        return jsonify(results=cur.fetchall())
        #return jsonify(results=self.db.config)
