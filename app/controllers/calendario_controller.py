from flask import Blueprint, jsonify, request
from flasgger import Swagger, swag_from

from bson.json_util import dumps

from app import app
from app.db import db_calendario

@app.route('/calendario/<campeonato>/', methods=['GET'])
@swag_from('conf/calendario.yml')
def calendario(campeonato):
	db = db_calendario.DBJogos()
	resultado = db.find({'tipo_campeonato': int(campeonato)})
	resposta = {}
	resposta['success'] = True
	resposta['response'] = resultado
	print(resultado.count())
	db.close()
	return dumps(resposta)

@app.route('/calendario/rodada', methods=['POST'])
@swag_from('conf/calendario_por_rodada.yml')
def calendario_por_rodada():
	data = request.json
	db = db_calendario.DBJogos()
	resposta = {}
	resposta['success'] = True
	resultado = db.find({'tipo_campeonato': int(data['campeonato']), 'rodada': int(data['rodada'])})
	resposta['response'] = resultado
	print(resultado.count())
	db.close()
	return dumps(resposta)