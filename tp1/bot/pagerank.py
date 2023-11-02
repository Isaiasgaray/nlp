from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import numpy as np
import spacy

# Cargar el modelo de spaCy
# !python -m spacy download es_core_news_md
nlp = spacy.load('es_core_news_md')

# Función para generar un resumen extractivo usando PageRank
def summarize(text, num_sentences=5):
    
    lemmatized_sentences = list()
    original_sentences   = list()
    doc = nlp(text)
    
    for sent in doc.sents:
        lemmatized_sentence = ' '.join(
                                        token.lemma_ for token in sent
                                        if not token.is_stop and 
                                        not token.is_punct)

        if lemmatized_sentence.strip() != '':
            lemmatized_sentences.append(lemmatized_sentence)
            original_sentences.append(str(sent).strip())

    # Procesar las oraciones lematizadas con spaCy para obtener sus vectores
    lemmatized_docs = [nlp(sent) for sent in lemmatized_sentences]

    # Obtenemos una lista con los vectores de cada oración
    sentence_vectors = [sent.vector for sent in lemmatized_docs]

    # Devuelve una matriz de similitud entre las oraciones filtradas
    similarity_matrix = cosine_similarity(sentence_vectors)
    
    # Crear un grafo a partir de la matriz de similitud
    nx_graph = nx.from_numpy_array(similarity_matrix)
    
    # Aplicar PageRank al grafo
    scores = nx.pagerank(nx_graph)
    
    # Ordenar las oraciones por su puntuación y seleccionar las mejores
    ranked_sentences = sorted(
                            (
                                (scores[i], s) for i, s
                                in enumerate(original_sentences)
                            ),
                            reverse=True)
    
    return ' '.join(ranked_sentences[i][1] for i in range(num_sentences))
