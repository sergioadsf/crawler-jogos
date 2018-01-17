from flask_script import Manager
from flask import Flask
from flasgger import Swagger
from apscheduler.schedulers.background import BackgroundScheduler

import os
from pymongo import MongoClient

app = Flask(__name__)
manager = Manager(app)
swagger = Swagger(app)
scheduler = BackgroundScheduler()

if('mongo_user' in os.environ):
	client = MongoClient('mongodb://{0}:{1}@ds141657.mlab.com:41657/campeonato'
		.format(os.environ.get('mongo_user'), os.environ.get('mongo_psw')))
else:
	print('no')
	client = MongoClient('localhost', 27017)

from app.controllers import  calendario_controller, classificacao_controller, grupo_controller
