import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from memory.memory_store import get_all_problems


model = SentenceTransformer("BAAI/bge-small-en")


def build_index():

    problems = get_all_problems()

    if len(problems) == 0:
        return None, None

    questions = [p[0] for p in problems]

    embeddings = model.encode(questions)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings).astype("float32"))

    return index, questions