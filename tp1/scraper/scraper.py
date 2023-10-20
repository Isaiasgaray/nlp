from bs4 import BeautifulSoup
from datetime import datetime
import requests
import locale

# Configuracion para formato de hora y fecha
LOCALE_AR = 'es_AR.UTF-8'
locale.setlocale(locale.LC_TIME, LOCALE_AR)

DATE_FORMAT = '%d de %B %Y %H:%Mhs'
# datetime.strptime('20 de octubre 2023', date_format)

URL = 'https://www.lacapital.com.ar/secciones/ultimo-momento.html'

# TODO
# r = requests.get(URL)
# soup = BeautifulSoup(r.text, 'lxml')

# TODO
# for link in soup.find_all('a', {'class': 'cover-link'}):
#     pass

def procesar_link(link):

    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'lxml')

    # Titulo
    titulo = soup.find('h1', {'class': 'nota-title'}).text.strip()

    # Categoria
    categoria = soup.find('div', {'class': 'breadcrumbs'})\
                    .find_all('span')[1]\
                    .text.strip()

    # Fecha
    fecha = soup.find('span', {'class': 'nota-fecha'}).text
    hora  = soup.find('span', {'class': 'nota-hora'}).text

    fecha_iso = datetime.strptime(fecha + ' ' + hora, DATE_FORMAT).isoformat()

    # Texto
    parrafos = list()

    for tag in soup.find_all('div', {'class': 'article-body'}):
        parrafos += tag.find_all('p')

    texto = '\n'.join(
                        parrafo.text.strip() for parrafo in parrafos
                        if parrafo.text and '>>' not in parrafo.text
                     )

    return titulo, texto, categoria, fecha_iso

link = 'https://www.lacapital.com.ar/politica/en-santa-fe-se-espera-un-escrutinio-mas-agil-este-domingo-n10095957.html'

# print(procesar_link(link))
