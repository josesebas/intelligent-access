from flask_restful import Resource, request
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
from bson.json_util import dumps, loads, default

class Roles(Resource):
    def __init__(self, **kwargs):
        self.log = Logger()
        self.conn = kwargs['conn']
    def get(self):
        cur = self.conn.mysql.connection.cursor()
        cur.execute("SELECT name, id FROM roles WHERE deleted_at is null")
        self.conn.mysql.connection.commit()
        return jsonify(code=200, data=cur.fetchall())
        #return jsonify(results=self.db.config)
