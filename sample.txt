from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

class person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt=18, description="The person's age")
    grade: str = Field(description="The person's grade in school")
    place: Optional[str] = Field(description="The person's place of residence")

parser = PydanticOutputParser(pydantic_object=person)
    
temp = PromptTemplate(
    template="Provide a  data like name age grade and {place}\n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = temp | model | parser

result = chain.invoke({'place':'India'})

print(result)