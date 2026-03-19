from repo_loader import load_repo
from vector_store import build_index, search_index
from answer_engine import generate_answer

data = load_repo(".")

print("Building search index...")
index, files = build_index(data)

query = input("Ask something about code: ")

results = search_index(query, index, files)

print("\nGenerating answer...\n")

answer = generate_answer(query, data, results)

print(answer)