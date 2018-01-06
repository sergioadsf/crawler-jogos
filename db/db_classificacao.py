import pymongo
from pymongo import MongoClient
import os

class DBClassificacao:
	
	def __init__(self):
		self.__conect()

	def __build_client(self):
		if('mongo_user' in os.environ):
			self.client = MongoClient('mongodb://{0}:{1}@ds141657.mlab.com:41657/campeonato'
				.format(os.environ.get('mongo_user'), os.environ.get('mongo_psw')))
		else:
			print('no')
			self.client = MongoClient('localhost', 27017)

	def __conect(self):
		self.__build_client()
		self.db = self.client.campeonato
		#self.collection = self.db.jogos
		self.classificacao = self.db.classificacao

	def save(self, classificacao):
		self.classificacao.insert_one(classificacao)

	def close(self):
		self.client.close()