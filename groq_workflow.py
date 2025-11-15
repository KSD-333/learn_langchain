from typing import TypedDict
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq

load_dotenv()

chat = ChatGroq(model="llama-3.3-70b-versatile")


class PromptState(TypedDict):
    prompt: str
    response: str


def call_groq(state: PromptState) -> PromptState:
    """Call Groq via LangChain `ChatGroq` and store the reply text."""
    question = state["prompt"]
    ai_msg = chat.invoke(question)
    state["response"] = ai_msg.content
    return state


# Build the LangGraph workflow
_graph = StateGraph(PromptState)
_graph.add_node("llm", call_groq)
_graph.add_edge(START, "llm")
_graph.add_edge("llm", END)
workflow = _graph.compile()


if __name__ == "__main__":
    
    example = {"prompt": "Explain quantum computing in 2 sentences for a beginner."}
    result = workflow.invoke(example)
    print(result["response"]) 
