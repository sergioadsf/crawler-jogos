from bs4 import BeautifulSoup
from urllib import request

def montar_info_equipe(equipes, tipo):
	valor = {}
	info = equipes.find('span', class_=("placar-jogo-equipes-%s"%(tipo)))
	sigla = info.find('span', class_="placar-jogo-equipes-sigla")
	nome = info.find('span', class_="placar-jogo-equipes-nome")
	img = info.find('img', class_=("placar-jogo-equipes-escudo-%s"%tipo))
	valor['sigla'] = str(sigla['title'])
	valor['nome'] = str(nome.text)
	valor['img'] = str(img['src'])
	return valor


proxy = request.ProxyHandler({'http': 'proxy.goias.gov.br:2303'})
opener = request.build_opener(proxy)
opener = request.build_opener(proxy)

num_rodada = 1
fo = open("calendario_goiano.html", "w")
while 1:
	html = request.urlopen(("http://globoesporte.globo.com/servico/esportes_campeonato/responsivo/widget-uuid/7f944f5c-e0b4-4c78-b0c1-54cb3c2e9c22/fases/primeira-fase-goiano-2017/rodada/%i/jogos.html"%num_rodada))
	soup = BeautifulSoup(html, 'html.parser')
	jogos_info = soup.find_all('li', class_='lista-de-jogos-item')

	if(not jogos_info):
		fo.close()
		print("FIM")
		exit()

	fo.write(" ------- RODADA DE Nº %i --------"%num_rodada)
	fo.write('\n')
	jogo = {}
	for jogo_info in jogos_info:
		info = jogo_info.find('div', class_="placar-jogo-informacoes")
		fo.write(str(info))
		meta = jogo_info.find(itemprop="startDate")
		jogo['data'] = str(meta['content'])
		fo.write('\n')
		for equipes in jogo_info.find_all('div', class_="placar-jogo-equipes"):
			mandante = montar_info_equipe(equipes, 'mandante')
			visitante = montar_info_equipe(equipes, 'visitante')
			fo.write(str(mandante))
			fo.write('\n')
			fo.write(str(visitante))
			fo.write('\n')
			fo.write('\n')
	num_rodada+=1
