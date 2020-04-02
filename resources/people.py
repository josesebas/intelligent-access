from flask_restful import Resource, request
from flask import jsonify, request as req, current_app as app

from libs.auth import auth
from libs.logger import Logger
from bson.json_util import dumps, loads, default

class People(Resource):
    def __init__(self, **kwargs):
        self.log = Logger()
        self.conn = kwargs['conn']
    def get(self, person_id=None):
        if person_id is None:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT people.created_at, updated_at, profile_person.* FROM people LEFT JOIN profile_person ON people.id = profile_person.person_id")
            self.conn.mysql.connection.commit()
            return jsonify({'code':200, 'data':cur.fetchall()})
        else:
            cur = self.conn.mysql.connection.cursor()
            cur.execute("SELECT people.created_at, updated_at, profile_person.* FROM people LEFT JOIN profile_person ON people.id = profile_person.person_id WHERE id = %s" %person_id)
            self.conn.mysql.connection.commit()
            return jsonify({'code':200, 'data':cur.fetchall()})
        #return jsonify(results=self.db.config)
