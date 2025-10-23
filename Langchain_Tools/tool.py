from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

search = DuckDuckGoSearchRun()

result = search.invoke("What is Langchain?")

print(result)

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b

res = multiply.invoke({"a": 3, "b": 4})  
print(res)

