from pymongo import MongoClient
import os

class DBJogos:
	
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
		self.jogos = self.db.jogos

	def save(self, jogo):
		self.jogos.insert_one(jogo)

	def save_all(self, lista_jogos):
		self.drop_collection()
		self.jogos.insert_many(lista_jogos)

	def find_all(self):
		return self.jogos.find()

	def find(self, filter):
		return self.jogos.find(filter)
	
	def drop_collection(self):
		self.jogos.drop()

	def close(self):
		self.client.close()