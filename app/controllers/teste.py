from flask import Flask
from flasgger import Swagger, swag_from

from bson.json_util import dumps

from app import app
from app.db import db_calendario

#app.load_src("db_calendario", "../db/db_calendario.py")
#import 

swagger = Swagger(app)

@app.route('/classificacao/<campeonato>/')
@swag_from('teste.yml')
def campeonato(campeonato):
	db = db_calendario.DBJogos()
	resultado = db.find({'tipo': int(campeonato)})
	print(resultado.count())
	db.close()
	return dumps(resultado)

app.run(debug=True)