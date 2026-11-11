from pathlib import Path 
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY ERROR")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-20b"


def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_prompt='''
This is a user complaint.
My laptop is not working.
Classify this.
'''
print(llm_ans(bad_prompt))

prompt='''
#ROLE
You are a support assistant at a mobile/laptop company.

#TASK
You have to classify the issue into categories

#CONSTRAINTS
You have to classify the issues into one of the three categories as : Technical,Billing,Return.

# OUTPUT FORMAT
The answer should be in one word only.The one word should be one of the categories mentioned in the constraints.
Output can be only REFUND,TECHNICAL,BILLING

#Example
Query:If user wants a refund then category will be Refund.
Query:If user has some problem with the product itself then the problem is technical.
Query:If user has some problem with billing then problem is billing.
Answer in one word only.

#FALLBACK
If the user asks any query other than mentioned categories then the reply with Other in one word.

I have problem with my laptop as it is not getting on.
'''

print(llm_ans(prompt))

# A good prompt has following things.
# 1.Role : Act as a senoir Ai enginner 
# 2.Clearly defined task
# 3.Constraints
# 4.Output Format 
# 5.Example
# 6.Fallback