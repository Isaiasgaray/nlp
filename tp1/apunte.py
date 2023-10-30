# !pip install spacy
# !python -m spacy download es_core_news_md

import spacy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity


# Función para generar un resumen extractivo usando PageRank
def summarize(similarity_matrix, num_sentences=5):
    # Crear un grafo a partir de la matriz de similitud
    nx_graph = nx.from_numpy_array(similarity_matrix)
    # Aplicar PageRank al grafo
    scores = nx.pagerank(nx_graph)
    # Ordenar las oraciones por su puntuación y seleccionar las mejores
    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(original_sentences)), reverse=True
    )
    return " ".join([ranked_sentences[i][1] for i in range(num_sentences)])


# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_md")

# Texto de ejemplo
text = """
Ciencia y Tecnología.\nEn esta sección, hablaremos de algo muy interesante. La inteligencia artificial (IA) se refiere a la simulación de la inteligencia humana en máquinas que están programadas para pensar y actuar como humanos. El término también puede aplicarse a cualquier máquina que exhiba rasgos asociados con la mente humana, como el aprendizaje y la resolución de problemas. La capacidad ideal de la inteligencia artificial es su habilidad para racionalizar y tomar acciones que tengan las mejores posibilidades de lograr un objetivo específico. Un subconjunto de la IA es el aprendizaje automático, que se refiere a conceptos en los que las máquinas aprenden por sí mismas sin estar programadas específicamente.
"""

doc = nlp(text)

# Lematizar y eliminar stopwords de cada oración
lemmatized_sentences = []
original_sentences = []
for sent in doc.sents:
    lemmatized_sentence = " ".join(
        [token.lemma_ for token in sent if not token.is_stop and not token.is_punct]
    )
    if lemmatized_sentence.strip() != "":  # Asegurarse de que la oración no esté vacía
        lemmatized_sentences.append(lemmatized_sentence)
        original_sentences.append(str(sent).strip())

# Procesar las oraciones lematizadas con spaCy para obtener sus vectores
lemmatized_docs = [nlp(sent) for sent in lemmatized_sentences]

# Obtenemos una lista con los vectores de cada oración
sentence_vectors = [sent.vector for sent in lemmatized_docs]

# Crear una matriz de similitud entre las oraciones filtradas
similarity_matrix = cosine_similarity(sentence_vectors)

# Generar resumen extractivo
resumen = summarize(similarity_matrix, num_sentences=2)
print("\nResumen Extractivo:")
print(resumen)
