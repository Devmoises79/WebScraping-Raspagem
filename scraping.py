import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?client=opera"

requisicao = requests.get(link)
print(requisicao)

print(requisicao.text) # pegando o html



site= BeautifulSoup(requisicao.text, "html.parser") # leitura do site
print(site.prettify()) # formatação


print(site.title) # pegar o título

titulo = site.find("title") # pegando o título de outra maneira
print(titulo)

pesquisa = site.find("input") # pegando o input
print(pesquisa)

pesquisa = site.find_all("input") # pegando todos os inputs
print(pesquisa)

pesquisa = site.find_all("input") # pegando todos os inputs
print(pesquisa [0])

pesquisa = site.find_all("input") # pegando todos os inputs
print(pesquisa [1])

