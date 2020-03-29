from flask_restful import Resource, request
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
from bson.json_util import dumps, loads, default

class Users(Resource):
    def __init__(self, **kwargs):
        self.log = Logger()
        self.conn = kwargs['conn']
    def get(self):
        cur = self.conn.mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        self.conn.mysql.connection.commit()
        users = cur.fetchall()
        for user in users:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT * FROM roles LEFT JOIN role_has_user ON role_has_user.role_id = roles.id WHERE user_id = %s" %user['id'])
            self.conn.mysql.connection.commit()
            user['roles']=cur.fetchall()
        return jsonify(code=200, data=users)
        #return jsonify(results=self.db.config)
