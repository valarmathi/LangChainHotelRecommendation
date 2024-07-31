from tenacity import retry, wait_random_exponential, stop_after_attempt
import openai
import json
import os

os.environ["OPENAI_API_KEY"] = "<>"

#from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain.schema.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from langchain_openai import ChatOpenAI
    
# Define a Chat Completions API call
# Retry up to 6 times with exponential backoff, starting at 1 second and maxing out at 20 seconds delay
@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_chat_completions(input, json_format = False):
    llm = OpenAI()
    #llm = OpenAI()

    output = llm(input)
    return output

def get_chat_response(system_message, user_message):
    llm_chat = ChatOpenAI()
    
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_message)
    ]

    response = llm_chat(messages)
    print('response ',response);
    return response