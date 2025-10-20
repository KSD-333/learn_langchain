from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

loader = PyPDFLoader(file_path="Practice Questions.pdf")
data = loader.load()


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

parser = StrOutputParser()


temp = PromptTemplate(
    template="Provide some basic info related to these code {topic}",
    input_variables=['topic']
)

chain = temp | model | parser

chain_result = chain.invoke({'topic':data[0].page_content})

print(chain_result)