from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
 
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
model2 = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
parser = StrOutputParser()
temp = PromptTemplate(
    template="Generate how i can earn money from {topic}in faster but safe and it should be one analyze market and according provide singlae solution",
    input_variables=['topic']
)
temp2 = PromptTemplate(
    template="Generate ideas on how to earn money from {topic2} in a faster but safe way. Analyze the market and provide a single comprehensive solution.",
    input_variables=['topic2']
)   

temp3 = PromptTemplate(
    template="Merge these two text and give me in points {text1} and {text2}",
    input_variables=['text1', 'text2']
)

paralle_chain = RunnableParallel({  
    "topic":temp | model | parser, 
    "topic2": temp2 | model2 | parser
})
result = paralle_chain.invoke({'topic':'Youtube', 'topic2':'Instagram'})
    
merge_chain = paralle_chain | temp3 | parser
print(merge_chain)