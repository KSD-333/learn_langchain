from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

temp = PromptTemplate(
    template="Provide some detailed info releted to {Topic}",
    input_variables=['Topic']
)

temp2 = PromptTemplate(
    template="Extreact key points and step from these {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = temp | model | parser | temp2 | model | parser

result = chain.invoke("how to devlop agent using langchain")

print(result)