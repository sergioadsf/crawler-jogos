import pymongo
from pymongo import MongoClient
import pprint

class DBJogos:
	
	def __init__(self):
		self.__conect()

	def __conect(self):
		self.client = MongoClient('localhost', 27017)
		self.db = self.client.campeonato
		self.collection = self.db.jogos
		self.jogos = self.db.jogos

	def save(self, jogo):
		pprint.pprint(jogo)
		self.jogos.insert_many(jogo)

	def close(self):
		self.client.close()