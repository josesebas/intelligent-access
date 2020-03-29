from flask import Flask, request as req, jsonify
from flask_restful import Resource, Api, request
from bson.json_util import dumps, loads, default
#archivos
from resources.access import Access
from libs.logger import Logger
from config.config import general as config
from libs.mysql import DB
app = Flask(__name__)
api = Api(app)
log = Logger()
conn = DB(app)

# Routes
#api.add_resource(Respondent, '/respondent','/respondent/<name>')
api.add_resource(Access, '/get-access', resource_class_kwargs={'conn':conn})
#-------
if __name__ == '__main__':
    log.info('Server listen in %s:%s' %(config['host'], config['port']))
    app.run(debug=True, host=config['host'], port=config['port'])
