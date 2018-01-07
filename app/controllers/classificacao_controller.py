from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

from bson.json_util import dumps

from app import app
from app.db import db_calendario

swagger = Swagger(app)

@app.route('/classificacao/<campeonato>/', methods=['GET'])
@swag_from('conf/classificacao.yml')
def campeonato(campeonato):
	db = db_calendario.DBJogos()
	resultado = db.find({'tipo': int(campeonato)})
	print(resultado.count())
	db.close()
	return dumps(resultado)

@app.route('/classificacao/rodada', methods=['POST'])
@swag_from('conf/classificacao_por_rodada.yml')
def classificacao_por_rodada():
	data = request.json
	db = db_calendario.DBJogos()
	resultado = db.find({'tipo': int(data['tipo']), 'rodada': int(data['rodada'])})
	print(resultado.count())
	db.close()
	return dumps(resultado)