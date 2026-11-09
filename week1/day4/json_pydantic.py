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

text='Hello my name is Sonu Kumar.I recently purchased an iphone from your store but it is not working now.My email is abc@gmail.com.I am from Delhi.'
prompt=f''' This is the customer ticket.Please extract personal information from this.{text}
'''

message={
    "role":role,
    "content":prompt,
}
messages=[message]
client=Groq(api_key=my_api_key)
response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)

    



#Above will give you unstructured output.



