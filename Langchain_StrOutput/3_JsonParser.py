from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

parser = JsonOutputParser()

temp = PromptTemplate(
    template="Provide a json format data like name age grade\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
chain = temp | model | parser

chain_result = chain.invoke({})

print(chain_result)