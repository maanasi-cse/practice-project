import os

def load_repo(path):
    code_data = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    code_data.append({
                        "file": file_path,
                        "content": content
                    })

    return code_data