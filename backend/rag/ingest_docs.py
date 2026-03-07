import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("BAAI/bge-small-en")

docs = []
vectors = []

KB_PATH = "../knowledge_base"


def chunk_text(text, chunk_size=200):

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


for file in os.listdir(KB_PATH):

    if not file.endswith(".md"):
        continue

    with open(os.path.join(KB_PATH, file), "r") as f:

        text = f.read()

        chunks = chunk_text(text)

        for chunk in chunks:

            docs.append(chunk)

            embedding = MODEL.encode(chunk)

            vectors.append(embedding)


vectors = np.array(vectors)

dimension = vectors.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(vectors)

faiss.write_index(index, "math_index.faiss")

np.save("docs.npy", docs)

print("Knowledge base indexed successfully")