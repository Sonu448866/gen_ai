import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import sys
import numpy as np
from sentence_transformers import SentenceTransformer


load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API KEY ISSUE")


client=Groq(api_key=my_api_key)

model="openai/gpt-oss-20b"



embedding_model=SentenceTransformer("all-MiniLM-L6-v2")

# Knowledge BAse
documents = [
    "Employees receive 24 days of paid leave per year.",
   
    "Employees work from the office on Tuesday, Wednesday and Thursday. "
    "Monday and Friday are optional work-from-home days.",
   
    "Employees receive Rs 3000 per month for gym reimbursement.",
   
    "Employees can claim Rs 2000 per month for home internet.",
   
    "Employees have a 90 day notice period."
]

document_embeddings = embedding_model.encode(documents)  # Creates a embedding of each lines of documents

print(sys.getsizeof(document_embeddings))  
# As there are 6 lines the size of it will be total byte size that is why we use vector database 
# as knowledge base can be huge.for current program it is enough but it can grow in GBs then your
# computer can't handle it that's why we use vector DB which is a specialized database for storing vector embeddings.
# Also here we are searching releavant context line by line for wach query which is not sacalable 
# and this problem is also solved by vector database.

# In this program even if there is no context the most score if it is negative will be given as a context to the LLM
# which is not relevant so in that case we can put some threshold below which the context will not be given 
# and you just resturn something like "Context Not Found"

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


# Finding in list of embedding which one is most close to the query embeddings
# The emnedding with highest similarity becomes the context
def retrieve(qembedding):
    scores = []  # (0.4,Lines from document)
    for i, document in  enumerate(document_embeddings):
        score=cosine_similarity(qembedding,document )
        scores.append((score,documents[i]))
    scores.sort(reverse=True)
    return scores[0]  # Returns socre as well as line from document



def ask_llm(question,context):

    sys_prompt=f"""answer in one line only. Answer only based on this context. do not hallucinate. Context: {context}"""
    system_message={
        "role": "system",
        "content": sys_prompt

    }
    message={
        "role": "user",
        "content": question
    }
    messages=[system_message, message]
    response=client.chat.completions.create(model=model, messages=messages)
    answer=response.choices[0].message.content
    return answer



query = "How much vacation do I get?"
qembedding=embedding_model.encode(query)

score,context=retrieve(qembedding)  # you will get score and contenxt 
print(score,context)

answer=ask_llm(query,context)
print(answer)