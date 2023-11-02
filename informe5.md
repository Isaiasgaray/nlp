En este ejercicio se realiza una extraccion de texto, con el fin de resumir noticias basandose en la categoria a la que pertencen estas.
Se usa un grafo como estructura de datos con la libreria networkX para hacer que cada oracion sea un nodo del grafo y la similitud calculada anteriormente entre cada palabra es la arista.

Por que no usamos modelos abstractivos?
Bart-Large-CNN: No esta optimizado para resumir noticias, resume bien textos en ingles.
MT5: Si bien se entreno para resumir noticias en varios idiomas incluyendo español, el problema es que el dataset de noticias en español es bastante chico, , los resultados ya resumidos presentan dificultad para ser entendidos o resumen demasiado la noticia
BLB-Spanish: presenta el mismo problema que el modelo anterior, si bien esta hecho con 290 mil noticias estas son solo de diarios españoles, los cuales presentan diferencias a los proporcionados por nosotros, por lo que los resumenes son poco entendibles o imprecisos.

Para obtener mejores resultados, es posible entrenar estos modelos con un dataset que contenga noticias más similares a las que se tienen disponible. Además, se puede ajustar o afinar los modelos (fine-tuning) para adaptarlos específicamente a las necesidades y características de las noticias en cuestión. Esto podría mejorar la calidad de los resúmenes generados y hacer que sean más relevantes y comprensibles para los usuarios.
