from flask import Flask, jsonify, request, make_response
from flasgger import Swagger, swag_from

from bson.json_util import dumps

from app import app
from app.db import db_classificacao

@app.route('/classificacao/<campeonato>/', methods=['GET'])
@swag_from('conf/classificacao.yml')
def classificacao(campeonato):
	db = db_classificacao.DBClassificacao()
	resultado = db.find({'tipo_campeonato': int(campeonato)})
	resposta = {}
	resposta['success'] = True
	resposta['response'] = resultado
	resp = make_response(dumps(resposta), code)
	resp.headers.extend({'content-type': 'application/json'})
	db.close()
	return resp

@app.route('/classificacao/grupo', methods=['POST'])
@swag_from('conf/classificacao_por_grupo.yml')
def classificacao_por_grupo():
	data = request.json
	db = db_classificacao.DBClassificacao()
	resposta = {}
	resposta['success'] = True
	resultado = db.find({'$and':[{'tipo_campeonato': int(data['campeonato']), 'grupo': data['grupo']}]})
	resposta['response'] = resultado
	db.close()
	return dumps(resposta)

@app.route('/classificacao/time', methods=['POST'])
@swag_from('conf/classificacao_time.yml')
def classificacao_time():
	data = request.json
	db = db_classificacao.DBClassificacao()
	resposta = {}
	resposta['success'] = True
	resultado = db.find({'$and':[{'tipo_campeonato': int(data['campeonato']), 'time_nome': data['time'].capitalize()}]})
	resposta['response'] = resultado
	db.close()
	return dumps(resposta)