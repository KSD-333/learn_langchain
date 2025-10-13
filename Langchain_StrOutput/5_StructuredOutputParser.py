from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

parser = StructuredOutputParser.from_response_schemas([
    ResponseSchema(name="name", description="The person's name"),
    ResponseSchema(name="grade", description="The person's grade or class in school"),
    ResponseSchema(name="age", description="The person's age in years"),
    ResponseSchema(name="place", description="The person's place of residence"),
])

temp = PromptTemplate(
    template="Generate information about a person from {place}. Include their name, age, grade, and place of residence.\n\n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
chain = temp | model | parser

chain_result = chain.invoke({'place':'India'})

print(chain_result)