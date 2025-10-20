from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()
url="https://en.wikipedia.org/wiki/Coding"
loader = WebBaseLoader(url)
data = loader.load()


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

parser = StrOutputParser()


temp = PromptTemplate(
    template="Provide ans of following question: {question}",
    input_variables=['question']
)

# chain = temp | model | parser

print(data[0].page_content)