import numpy as np
from sentence_transformers import SentenceTransformer

from memory.faiss_index import build_index
from memory.memory_store import get_all_problems


model = SentenceTransformer("BAAI/bge-small-en")


def find_similar_problem(query):

    index, questions = build_index()

    if index is None:
        return None

    query_vec = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vec, 1)

    idx = indices[0][0]

    problems = get_all_problems()

    return problems[idx]