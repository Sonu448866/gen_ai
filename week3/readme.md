steps to configure with uv:
1.uv init
2.uv venv
3..venv\Scripts\Activate.ps1
4.uv add python-dotenv qdrant-client sentence-transformers groq(install dependencies)

5.uv pip list(to see the list of packages)
6.uv pip freeze > requirements.txt (to genearte requirement.txt)

How to install dependencies from requirements.txt later?
1.uv venv
2..venv\Scripts\Activate.ps1
3.uv pip install -r requirements.txt
