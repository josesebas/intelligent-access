from flask_restful import Resource, request
from flask.views import MethodView
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
from bson.json_util import dumps, loads, default

class Roles(Resource, MethodView):
    def __init__(self, **kwargs):
        self.log = Logger()
        self.conn = kwargs['conn']
    def get(self, rol_id=None):
        if rol_id is None:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT name, id FROM roles")
            self.conn.mysql.connection.commit()
            return jsonify(code=200, data=cur.fetchall())
        else:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT name, id FROM roles WHERE id = %s" %rol_id)
            self.conn.mysql.connection.commit()
            return jsonify(code=200, data=cur.fetchall())

        #return jsonify(results=self.db.config)
