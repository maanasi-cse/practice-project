import faiss
import numpy as np
from embeddings import get_embedding

def build_index(data):
    embeddings = []
    files = []

    for item in data:
        emb = get_embedding(item["content"])
        embeddings.append(emb)
        files.append(item["file"])

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, files

def search_index(query, index, files):
    query_emb = np.array([get_embedding(query)]).astype("float32")

    distances, indices = index.search(query_emb, k=3)

    results = []
    for i in indices[0]:
        results.append(files[i])

    return results