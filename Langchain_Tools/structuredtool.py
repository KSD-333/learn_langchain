from langchain_community.tools import StructuredTool
from pydantic import BaseModel, Field



class AddNumbersInput(BaseModel):
    a: int 
    b: int 


def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b


stru_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply_numbers",
    description="Multiply two integers and return the result.",
    args_schema=AddNumbersInput
)

result = stru_tool.invoke({"a": 5, "b": 6})
print(result)