from flask_restful import Resource, request
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
from bson.json_util import dumps, loads, default

class Type_people(Resource):
    def __init__(self, **kwargs):
        self.log = Logger()
        self.conn = kwargs['conn']
    def get(self, type_id=None):
        if type_id is None:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT name, created_at, updated_at FROM type_people")
            self.conn.mysql.connection.commit()
            return jsonify(code=200, data=cur.fetchall())
        else:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT name, created_at, updated_at FROM type_people WHERE id = %s" %type_id)
            self.conn.mysql.connection.commit()
            return jsonify(code=200, data=cur.fetchall())
        #return jsonify(results=self.db.config)
