from flask import Flask, request as req, jsonify
from flask_restful import Resource, Api, request
from bson.json_util import dumps, loads, default
#models
from resources.access import Access
from resources.roles import Roles
from resources.users import Users
from resources.people import People
from resources.type_people import Type_people

from libs.logger import Logger
from config.config import general as config
from libs.mysql import DB
app = Flask(__name__)
api = Api(app)
log = Logger()
conn = DB(app)

# Routes
#api.add_resource(Respondent, '/respondent','/respondent/<name>')
api.add_resource(Access, '/access', resource_class_kwargs={'conn':conn})
api.add_resource(Roles, '/roles', resource_class_kwargs={'conn':conn})
api.add_resource(Users, '/users', resource_class_kwargs={'conn':conn})
api.add_resource(People, '/people', resource_class_kwargs={'conn':conn})
api.add_resource(Type_people, '/type_people', resource_class_kwargs={'conn':conn})

#-------
if __name__ == '__main__':
    log.info('Server listen in %s:%s' %(config['host'], config['port']))
    app.run(debug=True, host=config['host'], port=config['port'])
