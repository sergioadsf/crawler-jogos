from bs4 import BeautifulSoup
from urllib import request

proxy = request.ProxyHandler({'http': 'proxy.goias.gov.br:2303'})
opener = request.build_opener(proxy)


html = request.urlopen("http://globoesporte.globo.com/sp/futebol/campeonato-paulista/")
soup = BeautifulSoup(html, 'html.parser')
fo = open("classificacao.html", "w")
for tag in soup.find_all('section', class_='section-container'):
	groups = tag.find('h2').text
	fo.write(str(groups))
	for times in tag.find_all('table', class_="tabela-times"):
		fo.write('\n')
		for time in times.find_all('a'):
			fo.write(str(time.attrs['title']))
			fo.write('\n')
	for pontos in tag.find_all('table', class_="tabela-pontos"):
		for tr in pontos.find_all('tr', class_="tabela-head-linha"):
			for th in tr.find_all('th'):
				fo.write(str(th.text))
				fo.write('\n')
		for tr in pontos.find_all('tr', class_="tabela-body-linha"):
			for td in tr.find_all('td'):
				fo.write(str(td.text))
				fo.write('\n')
			fo.write('\n')
			
		#fo.write('PONTOS')
		#fo.write(str(pontos))
		fo.write('\n')
fo.close()

fo = open("jogos.html", "w")
for ul in soup.find_all('ul', class_='lista-de-jogos-conteudo'):
	for li in soup.find_all('li', class_='lista-de-jogos-item'):
		for meta in li.find_all('meta'):
			fo.write(str(meta['content']))
			fo.write('\n')
		fo.write('\n')
		
		for info in li.find_all('div', class_="placar-jogo-informacoes"):
			fo.write(str(info.text))
		
		for info_jogo in li.find_all('div', class_="placar-jogo-equipes"):
			for info_mandante in info_jogo.find_all('span', class_="placar-jogo-equipes-mandante"):
				fo.write('\n')
				mandante = info_mandante.find('span', class_="placar-jogo-equipes-sigla")
				fo.write('MANDANTE -> ' + str(mandante['title']) + ' - ' + str(mandante.text))

			for info_visitante in info_jogo.find_all('span', class_="placar-jogo-equipes-visitante"):
				fo.write('\n')
				visitante = info_visitante.find('span', class_="placar-jogo-equipes-sigla")
				fo.write('VISITANTE -> ' + str(visitante['title']) + ' - ' + str(visitante.text))

		fo.write('\n')

fo.close()

print("FIM")
