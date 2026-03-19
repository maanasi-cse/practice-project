def generate_answer(query, data, results):
    context = ""

    for file in results:
        for item in data:
            if item["file"] == file:
                context += item["content"][:500] + "\n\n"

    answer = f"""
Question: {query}

Relevant Code Snippets:
{context}

Explanation:
This code likely relates to your query. Review the above snippets for details.
"""
    return answer