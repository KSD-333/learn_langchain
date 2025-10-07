from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
messages = [
        SystemMessage(content="You are a helpful assistant and answer the given questions properly."),
]



while True:
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response = model.invoke(messages)
    print(response.content)
    messages.append(AIMessage(content=response.content))

print(messages)

"""
These are the message histories.
In these we  set one system message and from that we send human message and get message from ai through api and stored in like messages list.
it is only for learning that how to use message history in langchain with predefined message function in langchain.
"""
