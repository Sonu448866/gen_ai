from pathlib import Path
import os

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


load_dotenv()

class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()
response_format={
    "type": "json_object"
}
#json word should appear in the system prompt
system_prompt=f'''
Extract the personal information from the ticket based on 
on this schema and give me a json output.{schema}
'''
message_system={
    "role":"system",
    "content":system_prompt
}


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
messages=[message_system,message]
client=Groq(api_key=my_api_key)
response = client.chat.completions.create(model=model, messages=messages,response_format=response_format)
print(response.choices[0].message.content)

    
#How to read

import json
raw_json=response.choices[0].message.content
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)

