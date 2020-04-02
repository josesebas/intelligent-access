from flask_restful import Resource, request, reqparse
from flask.views import MethodView
import json
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
from bson.json_util import dumps, loads, default

parser = reqparse.RequestParser()

class Access(Resource, MethodView):
    def __init__(self, **kwargs):
        self.log = Logger()
        self.conn = kwargs['conn']
    def get(self, access_id=None):
        if access_id is None:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT name, created_at, updated_at FROM access")
            self.conn.mysql.connection.commit()
            return jsonify(code=200, data=cur.fetchall())
        else:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT name, created_at, updated_at FROM access WHERE id = %s" %access_id)
            self.conn.mysql.connection.commit()
            return jsonify(code=200, data=cur.fetchall())
            #return jsonify(results=self.db.config)

    def put(self, access_id=None):
        if access_id is None:
            return jsonify(code=403)
        else:
            parser.add_argument('data', action='append')
            args = parser.parse_args()
            args = json.loads(args['data'][0])
            cur = self.conn.mysql.connection.cursor()
            cur.execute("UPDATE access set name=%s WHERE id = %s",(args['name'],access_id))
            self.conn.mysql.connection.commit()
            return jsonify(args)

    def post(self, access_id=None):
        if access_id is None:
            return jsonify(code=403)
        else:
            parser.add_argument('data', action='append')
            args = parser.parse_args()
            args = json.loads(args['data'][0])
            #cur = self.conn.mysql.connection.cursor()
            #cur.execute("UPDATE access set name=%s WHERE id = %s",(args['name'],access_id))
            #self.conn.mysql.connection.commit()
            return jsonify(args)
    def delete(self, access_id=None):
        if access_id is None:
            return jsonify(code=403)
        else:
            parser.add_argument('data', action='append')
            args = parser.parse_args()
            args = json.loads(args['data'][0])
            #cur = self.conn.mysql.connection.cursor()
            #cur.execute("UPDATE access set name=%s WHERE id = %s",(args['name'],access_id))
            #self.conn.mysql.connection.commit()
            return jsonify(args)
