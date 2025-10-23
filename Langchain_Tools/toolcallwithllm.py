
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result"""
    return a * b



llm_tool =model.bind_tools([multiply])

# result = llm_tool.invoke('multiply 3 by 10')    
result = multiply.invoke({"a": 3, "b": 10})
print(result)

# Tool Binding with LLM