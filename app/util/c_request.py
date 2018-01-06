from bs4 import BeautifulSoup
from urllib import request
import os

def __ajustar_proxy():
	if('w_proxy' in os.environ and 'w_proxy_port' in os.environ):
		proxy_str = ('%s:%s' %(os.environ.get('w_proxy'), os.environ.get('w_proxy_port')) )
		proxy = request.ProxyHandler({'http': proxy_str})
		opener = request.build_opener(proxy)


def get_html(url):
	__ajustar_proxy()
	html = request.urlopen(url)
	return BeautifulSoup(html, 'html.parser')