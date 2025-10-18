from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")


parser = StrOutputParser()

temp = PromptTemplate(
    template="Generate ideas on how to earn money from {topic} in a faster but safe way. Analyze the market and provide a single comprehensive solution.",
    input_variables=['topic']
)

temp2 = PromptTemplate(
    template="Extract key points and actionable steps from the following text:\n\n{text}\n\nProvide a clear, organized list of steps.",
    input_variables=['text']
)

chain = temp | model | parser | temp2 | model | parser
result = chain.invoke({'topic':'Youtube'})
print(result)

chain.get_graph().print_ascii()