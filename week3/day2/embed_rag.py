import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer   #Hugging face open source models


def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

model=SentenceTransformer("all-MiniLM-L6-V2")  #384 features embeddings vectors
text="Machine learning is fun"

embedding=model.encode(text)
print(embedding.shape)
print(embedding)

t1="there are 24 paid leaves"
t2="there are 24 vacation days"

#Both are different

v1=model.encode(t1)
v2=model.encode(t2)

ans=cosine_similarity(v1,v2)
print(ans)