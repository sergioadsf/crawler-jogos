from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

from bson.json_util import dumps

from app import app
from app.db import db_classificacao

@app.route('/grupo/<campeonato>/', methods=['GET'])
@swag_from('conf/grupo_classificacao.yml')
def grupo_classificacao(campeonato):
	db = db_classificacao.DBClassificacao()
	resultado = db.distinct('grupo',{'tipo_campeonato': int(campeonato)})
	resposta = {}
	resposta['success'] = True
	resposta['response'] = resultado
	db.close()
	return dumps(resposta)