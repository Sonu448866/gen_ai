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

# Step 1
knowlege_base={
    "youtube_channel":"Defence Matrix",
    "name":"Durgesh Bhai",
    "work":"Profficient in alalysis of defence things and has youtube channel.Sometimes he roast pakistani army and their people"
}

# Step 2: Retrieval from Knowledge Base
def retrieve_info(question):
    question=question.lower()
    if "name" in question:
        return knowlege_base["name"]
    elif "work" in question:
        return knowlege_base["work"]
    elif "youtube_channel" in question:
        return knowlege_base["youtube_channel"]
    else:
        return None

    
def ask_llm(question):
    context=retrieve_info(question)  #Passing the context to LLM

    sys_prompt=f"""answer in one line only. Answer only based on this context. do not hallucinate. Context: {context}"""
   
    sys_message={
        "role":"system",
        "content":sys_prompt

    }
    message={
        "role":"user",
        "content":question
    }
    messages=[sys_message,message]

    response=client.chat.completions.create(model=model,messages=messages) # LLM Generation
    answer=response.choices[0].message.content
    return answer


question='''
Do you know youtube_channel Defence Matrix?    
'''
# Above works but when question is "Do you know youtube channel Defence Matrix?"  the above will not work as key doesn't match
# Even if you put lot of regular expression it can't work properly
print(ask_llm(question))


# But the probblem with above is knowlege Base and Retrieval as you can't put all the data in form of dictionary 
# and retrieval is not upto point as it is based on key search not semantic search or anything .As if we search "what does Defence Matrix do?" 
# Then it will not able to answer as question hasn't exact words that matches with the key of the knowdgebase dictionary.
