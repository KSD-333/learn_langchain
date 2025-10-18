from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnablePassthrough
from langchain.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Explain in detail about the {topic} ",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Explain in short about the {topic} ",
    input_variables=["topic"],
)


chain = prompt | model | parser

conditional_chain = RunnableBranch(
        (lambda x: len(x)>300, prompt2 | model | parser),
        RunnablePassthrough(),
    )

finally_chain = chain | conditional_chain

result = finally_chain.invoke({"topic": "Artificial Intelligence"})
print(result)