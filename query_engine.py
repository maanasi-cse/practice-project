import numpy as np
from embeddings import get_embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, data):
    query_emb = get_embedding(query)

    scores = []

    for item in data:
        code_emb = get_embedding(item["content"])
        score = cosine_similarity(query_emb, code_emb)
        scores.append((score, item["file"]))

    scores.sort(reverse=True)

    return scores[:3]