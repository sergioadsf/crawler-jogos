import pymongo
from pymongo import MongoClient
import os

class DBJogos:
	
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
		self.jogos = self.db.jogos

	def save(self, jogo):
		self.jogos.insert_one(jogo)

	def close(self):
		self.client.close()