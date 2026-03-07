import numpy as np
from sentence_transformers import SentenceTransformer
from rag.build_index import build_rag_index

model = SentenceTransformer("BAAI/bge-small-en")

index, docs = build_rag_index()


def retrieve_context(query, k=3):

    if index is None or len(docs) == 0:
        return []

    query_vec = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vec, k)

    context = []

    for i in indices[0]:

        if i < len(docs):
            context.append(docs[i])

    return context