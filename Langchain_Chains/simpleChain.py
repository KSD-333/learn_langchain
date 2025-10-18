from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
parser = StrOutputParser()
temp = PromptTemplate(
    template="Generate how i can earn money from {topic}in faster but safe and it should be one analyze market and according provide singlae solution",
    input_variables=['topic']
)
chain = temp | model | parser
result = chain.invoke({'topic':'Youtube'})
print(result)

chain.get_graph().print_ascii()