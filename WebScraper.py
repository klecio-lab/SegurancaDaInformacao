from bs4 import BeautifulSoup

import requests

#objeto site recebendo todo o conteudo da requesição http do site...
site = requests.get('https://www.climatempo.com.br/').content #'https://www.climatempo.com.br/' --- 'https://empire.goodgamestudios.com/'

#objeto soup baixado do site o html
soup = BeautifulSoup(site, 'html.parser')

#transforma o html em string e o print vai exibir o html
#print(soup.prettify())

temperatura = soup.find('div',class_="_margin-l-20 _flex-column")

print(temperatura.string)
print(soup.title.string)
print(soup.find('admin'))
