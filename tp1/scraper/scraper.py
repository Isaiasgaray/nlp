from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import locale

# Configuracion para formato de hora y fecha
LOCALE_AR = 'es_AR.UTF-8'
locale.setlocale(locale.LC_TIME, LOCALE_AR)

DATE_FORMAT = '%d de %B %Y %H:%Mhs'

# Funciones para procesar los links
def procesar_titulo(soup):
    return soup.find('h1', {'class': 'nota-title'}).text.strip()

def procesar_categoria(soup):
    return soup.find('div', {'class': 'breadcrumbs'})\
               .findChildren()[2].text.strip()

def procesar_fecha(soup):
    fecha = soup.find('span', {'class': 'nota-fecha'}).text
    hora  = soup.find('span', {'class': 'nota-hora'}).text

    return datetime.strptime(fecha + ' ' + hora, DATE_FORMAT).isoformat()


def procesar_contenido(soup):

    parrafos = list()

    for tag in soup.find_all('div', {'class': 'article-body'}):
        parrafos += tag.find_all('p')

    texto = '\n'.join(
                        parrafo.text.strip() for parrafo in parrafos
                        if parrafo.text and '>>' not in parrafo.text
                     )

    return texto

def procesar_link(link):

    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'lxml')

    try:
        titulo    = procesar_titulo(soup)
        texto     = procesar_contenido(soup)
        categoria = procesar_categoria(soup)
        fecha     = procesar_fecha(soup)

    except Exception as e:
        print(f'{link} => {e}')
        return tuple([None] * 5)

    return titulo, texto, categoria, link, fecha

# Funcion principal
def main():
    URL = 'https://www.lacapital.com.ar/secciones/ultimo-momento.html'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')

    columnas = ['titulo', 'texto', 'categoria', 'url', 'fecha']
    datos    = list()

    for tag in soup.find_all('a', {'class': 'cover-link'}):
        datos.append(procesar_link(tag.get('href')))

    df = pd.DataFrame(datos, columns=columnas)
    df.drop_duplicates(inplace=True)

    print(df)


if __name__ == '__main__':
    main()
