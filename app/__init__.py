from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

if('mongo_user' in os.environ):
	client = MongoClient('mongodb://{0}:{1}@ds141657.mlab.com:41657/campeonato'
		.format(os.environ.get('mongo_user'), os.environ.get('mongo_psw')))
else:
	print('no')
	client = MongoClient('localhost', 27017)

from app.controllers import teste
