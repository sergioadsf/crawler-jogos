from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime
import os

from db import db_calendario

from util import tipos, c_request

def __escrever_no_arquivo(arquivo, jogo):
	arquivo.write(str(jogo))
	arquivo.write('\n')
	arquivo.write('\n')

def __escrever_no_banco(db, jogo):
	db.save(jogo)

def __montar_info_equipe(equipes, tipo, jogo):
	valor = {}
	info = equipes.find('span', class_=("placar-jogo-equipes-%s"%(tipo)))
	sigla = info.find('span', class_="placar-jogo-equipes-sigla")
	nome = info.find('span', class_="placar-jogo-equipes-nome")
	img = info.find('img', class_=("placar-jogo-equipes-escudo-%s"%tipo))
	resultado = equipes.find('span', class_="placar-jogo-equipes-placar")
	gols = resultado.find('span', class_=("placar-jogo-equipes-placar-%s"%tipo))

	valor['sigla'] = str(sigla['title'])
	valor['nome'] = str(nome.text)
	valor['img'] = str(img['src'])
	valor['gols'] = str(gols.text)
	jogo[tipo] = valor

def preencher_info_estadio(jogo_info, jogo):
	info = jogo_info.find('div', class_="placar-jogo-informacoes")
	estadio = info.find('span', class_="placar-jogo-informacoes-local").text
	
	jogo['info'] = str(info.text).replace(estadio, '')
	jogo['estadio'] = estadio

def __executar(url, arquivo_nome, tipo_campeonato):
	num_rodada = 1
	fo = open(arquivo_nome, "w")
	db = db_calendario.DBJogos()
	while 1:
		soup = c_request.get_html("http://globoesporte.globo.com/servico/esportes_campeonato/responsivo/widget-uuid/%s"%(str(url).format(num_rodada)))
		jogos_info = soup.find_all('li', class_='lista-de-jogos-item')

		if(not jogos_info):
			fo.close()
			#print("FIM")
			db.close()
			return

		fo.write(" -------------- RODADA DE Nº %i --------------"%num_rodada)
		fo.write('\n')
		for jogo_info in jogos_info:
			jogo = {}
			jogo['rodada'] = num_rodada
			jogo['tipo'] = tipo_campeonato.value
			preencher_info_estadio(jogo_info, jogo)

			meta = jogo_info.find(itemprop="startDate")
			jogo['data'] = datetime.strptime(str(meta['content']), '%Y-%m-%d')
			fo.write('\n')
			for equipes in jogo_info.find_all('div', class_="placar-jogo-equipes"):
				mandante = __montar_info_equipe(equipes, 'mandante', jogo)
				visitante = __montar_info_equipe(equipes, 'visitante', jogo)
				
				#__escrever_no_arquivo(fo, jogo)
				__escrever_no_banco(db, jogo)
		num_rodada+=1

def executar():
	__executar("2776d78a-38ac-4982-85b1-2389ff26f468/fases/primeira-fase-campeonato-paulista-2018/rodada/{0}/jogos.html", "db/calendario-paulista.json", tipos.TipoCampeonato.PAULISTA)
	__executar("2bcee051-4e56-4ef5-94a4-e0a475ba56dd/fases/primeira-fase-campeonato-carioca-2018/grupo/2057/rodada/{0}/jogos.html", "db/calendario-carioca.json", tipos.TipoCampeonato.CARIOCA)
	__executar("7f944f5c-e0b4-4c78-b0c1-54cb3c2e9c22/fases/primeira-fase-goiano-2017/rodada/{0}/jogos.html", "db/calendario-goiano.json", tipos.TipoCampeonato.GOIANO)

executar()	
