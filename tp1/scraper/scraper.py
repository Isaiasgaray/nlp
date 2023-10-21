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

    try:
        # Titulo
        titulo = soup.find('h1', {'class': 'nota-title'}).text.strip()

        # Categoria
        # categoria_div = soup.find('div', {'class': 'breadcrumbs'})\
        #                     .find_all('span')

        # if len(categoria_div) != 3:
        #     categoria = 'Sin categoría'
        # else:
        #     categoria = categoria_div[1].text.strip()

        categoria = soup.find('div', {'class': 'breadcrumbs'})\
                        .findChildren()[2].text.strip()

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

    except Exception as e:
        print(f'{link} -----> {e}')
        return tuple([None] * 5)

    return titulo, texto, categoria, link, fecha_iso

def main():

    r = requests.get(URL)

    soup = BeautifulSoup(r.text, 'lxml')

    for tag in soup.find_all('a', {'class': 'cover-link'}):

        pass

if __name__ == '__main__':
    main()
