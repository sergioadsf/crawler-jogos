from pymongo import MongoClient
import os
#from app import client -- Migrar para client do app

class DBClassificacao:
	
	def __init__(self):
		self.__conect()

	def __build_client(self):
		if('mongo_user' in os.environ):
			self.client = MongoClient('mongodb://{0}:{1}@ds245357.mlab.com:45357/campeonato'
				.format(os.environ.get('mongo_user'), os.environ.get('mongo_psw')))
		else:
			self.client = MongoClient('localhost', 27017)

	def __conect(self):
		self.__build_client()
		self.db = self.client.campeonato
		#self.collection = self.db.jogos
		self.classificacao = self.db.classificacao

	def save(self, classificacao):
		self.classificacao.insert_one(classificacao)

	def save_all(self, lista_classificacao):
		self.drop_collection()
		self.classificacao.insert_many(lista_classificacao)

	def find_all(self):
		return self.classificacao.find()

	def find(self, filter):
		return self.classificacao.find(filter)

	def distinct(self, distinct_field, filter):
		return self.classificacao.distinct(distinct_field, filter)

	def drop_collection(self):
		self.classificacao.drop()

	def close(self):
		self.client.close()