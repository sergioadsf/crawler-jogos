from flask import Flask, jsonify, request
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
	db.close()
	return dumps(resposta)