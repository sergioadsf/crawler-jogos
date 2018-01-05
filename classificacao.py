from bs4 import BeautifulSoup
from urllib import request

from util import c_request

soup = c_request.get_html("http://globoesporte.globo.com/sp/futebol/campeonato-paulista/")
fo = open("db/classificacao.html", "w")

lista_classificacao = []
pos_grupo = 0
for grupo in soup.find_all('section', class_="section-container"):
	classificacao = {}
	classificacao['grupo'] = grupo.find('h2', class_="tabela-header-titulo").text
	#fo.write('---------------- %s ----------------' %classificacao['grupo'])
	#fo.write('\n')
	tab_time = grupo.find('table', class_="tabela-times")
	times = tab_time.find_all('tr', class_="tabela-body-linha")
	for pos_time in range(1, len(times)+1):
		posicao = times[pos_grupo].find('td', class_="tabela-times-posicao")
		classificacao['posicao'] = posicao.text
		classificacao['estilo'] = posicao.get('style')
		time = times[pos_grupo].find('td', class_="tabela-times-time")
		time_link = time.find('a', class_="tabela-times-time-link")
		classificacao['link'] = time_link['href']
		classificacao['time_nome'] = time_link['title']
		classificacao['alias'] = time_link.find('span', class_="tabela-times-time-sigla").text
		classificacao['variacao'] = times[pos_grupo].find('td', class_="tabela-times-variacao").text
		lista_classificacao.append(str(classificacao))
	pos_grupo += 1

fo.write(str(lista_classificacao))
fo.close()