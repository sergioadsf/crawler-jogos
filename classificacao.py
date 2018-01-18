from bs4 import BeautifulSoup
from urllib import request

from util import c_request, tipos
from db import db_classificacao

def __escrever_no_arquivo(arquivo, classificacao):
	arquivo.write(str(classificacao))
	arquivo.write('\n\n')

def __escrever_no_banco(db, classificacao):
	db.save(classificacao)

def __preencher_pontuacao(linha, pos, classificacao):
	pontos = linha[pos].find_all('td')
	classificacao['pontos'] = int(pontos[0].text)
	classificacao['jogos'] = int(pontos[1].text)
	classificacao['vitorias'] = int(pontos[2].text)
	classificacao['empates'] = int(pontos[3].text)
	classificacao['derrotas'] = int(pontos[4].text)
	classificacao['gols_pro'] = int(pontos[5].text)
	classificacao['gols_contra'] = int(pontos[6].text)
	#classificacao['saldo_gols'] = int(pontos[7].text)
	#classificacao['perc_ult_jogos'] = float(pontos[8].text)

def __preencher_times(linha, pos, classificacao):
	time = linha[pos].find('td', class_="tabela-times-time")
	time_link = time.find('a', class_="tabela-times-time-link")
	#classificacao['link'] = time_link['href']
	classificacao['time_nome'] = time_link['title']
	classificacao['alias'] = time_link.find('span', class_="tabela-times-time-sigla").text
	#classificacao['variacao'] = float(linha[pos].find('td', class_="tabela-times-variacao").text)

def __preencher_posicao(linha, pos, classificacao):
	posicao = linha[pos].find('td', class_="tabela-times-posicao")
	classificacao['posicao'] = posicao.text
	#classificacao['estilo'] = posicao.get('style')

def __preencher_grupo(grupo, classificacao):
	classificacao['grupo'] = grupo.find('h2', class_="tabela-header-titulo").text

def __qtd_times(linha):
	return range(0, len(linha))

def __executar(url_site, url_arquivo, tipo_campeonato):
	soup = c_request.get_html(url_site)
	fo = open(url_arquivo, "w")
	db = db_classificacao.DBClassificacao()

	pos_grupo = 0
	for grupo in soup.find_all('section', class_="section-container"):
		tab_time = grupo.find('table', class_="tabela-times")
		tab_pontos = grupo.find('table', class_="tabela-pontos")
		linha_times = tab_time.find_all('tr', class_="tabela-body-linha")
		linha_pontos = tab_pontos.find_all('tr', class_="tabela-body-linha")
		for pos_time in __qtd_times(linha_times):
			classificacao = {}
			classificacao['tipo'] = tipo_campeonato.value
			__preencher_grupo(grupo, classificacao)
			__preencher_posicao(linha_times, pos_time, classificacao)
			__preencher_times(linha_times, pos_time, classificacao)
			__preencher_pontuacao(linha_pontos, pos_time, classificacao)

			#__escrever_no_arquivo(fo, classificacao)
			__escrever_no_banco(db, classificacao)
		pos_grupo += 1

	fo.close()
	db.close()

def executar():
	__executar("http://globoesporte.globo.com/servico/esportes_campeonato/responsivo/widget-uuid/2776d78a-38ac-4982-85b1-2389ff26f468/fases/primeira-fase-campeonato-paulista-2018/classificacao.html", "db/classificacao_paulista.json", tipos.TipoCampeonato.PAULISTA)
	__executar("http://globoesporte.globo.com/servico/esportes_campeonato/responsivo/widget-uuid/2bcee051-4e56-4ef5-94a4-e0a475ba56dd/fases/primeira-fase-campeonato-carioca-2018/classificacao.html", "db/classificacao_carioca.json", tipos.TipoCampeonato.CARIOCA)
	__executar("http://globoesporte.globo.com/servico/esportes_campeonato/responsivo/widget-uuid/7f944f5c-e0b4-4c78-b0c1-54cb3c2e9c22/fases/primeira-fase-goiano-2017/classificacao.html", "db/classificacao_goiano.json", tipos.TipoCampeonato.GOIANO)

executar()