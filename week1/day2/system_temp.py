from pathlib import Path
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY ERROR")

model="openai/gpt-oss-20b"
role="user"
prompt="What is Dictionary?"

message_system={
    "role":"system",
    "content":'''You are a coding assistant cum code reviewer.You need to give answer to those questions only that are releated to coding.
    If someone asks you unreleated question then give reply that i can coding assistant.
    E.g .
    Q.What is an array?
    Ans:Array is a linear data structure that stores data in contniious manner.

    Q.What is Mobile?
    Ans:I am a coding assistant.I can't help you in this question.
    '''
    

}
message={
    "role":role,
    "content":prompt,
}
messages=[message_system,message]
client=Groq(api_key=my_api_key)



response = client.chat.completions.create(model=model, messages=messages,temperature=0)
print(response.choices[0].message.content)