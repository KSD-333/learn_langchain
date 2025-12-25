from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv 
import sqlite3
import os

# Load .env first
load_dotenv()

# Explicitly set LangSmith tracing - force it to be enabled
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "My CHATBOT Project")
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

# Verify API key is loaded
api_key = os.getenv("LANGCHAIN_API_KEY")

model = ChatGroq(model="llama-3.3-70b-versatile")
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    message: Annotated[list[BaseMessage], add_messages]

def Chat(state: ChatState):
    message = state['message']
    response = model.invoke(message)
    return {'message': [response]}

graph = StateGraph(ChatState)
graph.add_node('Chat', Chat)
graph.add_edge(START, "Chat")
graph.add_edge("Chat", END)
from langgraph.checkpoint.sqlite import SqliteSaver

conn = sqlite3.connect('chatbot_checkpoints.db', check_same_thread=False)

checkpoint = SqliteSaver(conn=conn)
app = graph.compile(checkpointer=checkpoint)


def get_all_threads():
    all_thread = set()
    for chekpoint in checkpoint.list(None):
        thread_name = chekpoint.config['configurable']['thread_id']
        all_thread.add(thread_name)
    return list(all_thread)
