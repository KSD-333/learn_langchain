from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Explain the concept of langchain in a simple way.")
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(response.content)
