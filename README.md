# 🌐 Web Scraping com Python (Requests + BeautifulSoup)

Projeto em Python voltado para raspagem de dados web, utilizando requests para requisições HTTP e BeautifulSoup para parsing e extração de elementos HTML.

## 🎯 Objetivo
Demonstrar fundamentos de web scraping, incluindo requisições HTTP, leitura de HTML e extração de dados estruturados a partir de páginas web.

## ⚙️ Funcionalidades
- Requisição HTTP para páginas web
- Leitura do HTML bruto da página
- Parsing e formatação do HTML
- Extração de elementos como título e inputs
- Busca de elementos específicos com find e find_all

## 🧠 Conceitos aplicados
- HTTP requests e resposta de servidor
- Estruturação e leitura de HTML
- Parsing de DOM com BeautifulSoup
- Seletores básicos de elementos HTML
- Manipulação e extração de dados não estruturados

## 🛠️ Tecnologias utilizadas
- Python
- Requests
- BeautifulSoup4

## 🚧 Limitações
- Uso de páginas dinâmicas não suportadas (JavaScript-heavy)
- Raspagem básica sem tratamento de anti-bot ou headers avançados
- Estrutura de dados não organizada (apenas impressão em console)
- Dependente da estrutura atual do HTML

## ⚠️ Observação técnica
O exemplo utiliza uma URL de busca, que pode retornar conteúdo dinâmico ou protegido, o que limita a extração consistente de dados estruturados.

## 🚀 Possíveis melhorias
- Implementação de headers e user-agent para requisições
- Uso de Selenium para páginas dinâmicas
- Estruturação dos dados em JSON ou CSV
- Tratamento de erros HTTP (status codes)
- Pipeline de coleta e armazenamento de dados

## 👨‍💻 Autor
Desenvolvido por Devmoises79  
Projeto com foco em introdução a web scraping e manipulação de dados HTML em Python.
