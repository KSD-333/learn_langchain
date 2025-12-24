from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv 

load_dotenv()

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
from langgraph.checkpoint.memory import InMemorySaver

checkpoint = InMemorySaver()
app = graph.compile(checkpointer=checkpoint)