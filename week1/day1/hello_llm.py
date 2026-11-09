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
prompt="Do you know Mahatma Gandhi?"
message={
    "role":role,
    "content":prompt,
}
messages=[message]
client=Groq(api_key=my_api_key)



response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)
