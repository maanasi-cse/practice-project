import streamlit as st
from repo_loader import load_repo
from vector_store import build_index, search_index
from answer_engine import generate_answer

st.title("💡 AI Codebase Assistant")

data = load_repo(".")
index, files = build_index(data)

query = st.text_input("Ask a question about your code:")

if query:
    results = search_index(query, index, files)
    answer = generate_answer(query, data, results)

    st.write("### Answer:")
    st.write(answer)