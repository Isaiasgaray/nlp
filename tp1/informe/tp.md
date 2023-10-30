# Enlaces

- [Link al repositorio](https://github.com/Isaiasgaray/nlp)
- [Link al bot de Telegram](https://t.me/tuia_nlp_bot)

# Creación del dataset
Para este trabajo práctico vamos a obtener los datos de la página web del diario **La Capital**. En esta web se puede realizar el scraping de forma sencilla, ya que no hace falta loguearse ni interactuar con **JavaScript** para acceder al HTML con el texto de las noticias, por lo tanto solamente necesitamos usar las librearías `requests` y `beautifulsoup4`.

Para obtener los datos de interés usamos la sección de *Últimas Noticias* del sitio. En esta sección hay aproximadamente 150 links a noticias. El script itera sobre cada uno de estos links para acceder a ellos con `requests`. En cada noticia se obtiene el *título*, *texto*, *categoría*, *url* y *fecha* de la misma. Consideramos que es útil almacenar la fecha en la que se publicó la noticia porque puede servir para generar un resumen por categoría y fecha de las noticias para el ejercicio 5.

Además la fecha de la noticia sirve para que el scraper ignore noticias que no sean del día actual, esta verificación es útil porque se podría correr el script diariamente y actualizar el dataset con las nuevas noticias del día.

# Clasificador de títulos

# Importancia de palabras por categoría

# Similitud de títulos en la categoría X

# Resumen de noticias con modelo X
