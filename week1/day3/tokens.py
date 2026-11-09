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
prompt1="Hi!!"
prompt2="Explain time travel in detail."
prompt3="Write 1000 words essay on Machine Learning."

prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
    "role":role,
    "content":prompt,
}
    messages=[message]
    client=Groq(api_key=my_api_key)
    response = client.chat.completions.create(model=model, messages=messages,max_tokens=50)
    print(response.choices[0].message.content)
    usage=response.usage
    print(usage.prompt_tokens)
    print(usage.completion_tokens)
    print(usage.total_tokens)
    print(f'Finish Reason:{response.choices[0].finish_reason}')  #If finish reason stop then terminated normally else due to max_tokens length
    print("####################")
    








