import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("BAAI/bge-small-en")


def load_documents():

    # Find project root
    current_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.abspath(os.path.join(current_dir, "../../"))

    kb_path = os.path.join(project_root, "knowledge_base")

    docs = []

    if not os.path.exists(kb_path):

        print("❌ Knowledge base folder not found:", kb_path)

        return docs

    print("📚 Loading knowledge base from:", kb_path)

    for root, _, files in os.walk(kb_path):

        for file in files:

            if file.endswith(".txt") or file.endswith(".md"):

                path = os.path.join(root, file)

                try:

                    with open(path, "r", encoding="utf-8") as f:

                        text = f.read().strip()

                        if len(text) > 10:

                            docs.append(text)

                except Exception as e:

                    print("Error reading:", path, e)

    print(f"✅ Loaded {len(docs)} knowledge documents")

    return docs


def build_rag_index():

    docs = load_documents()

    if len(docs) == 0:

        print("⚠ No knowledge base documents found")

        return None, []

    embeddings = model.encode(docs)

    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(embeddings)

    return index, docs