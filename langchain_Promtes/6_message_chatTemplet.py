from langchain_core.prompts import ChatPromptTemplate


template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("human", "{input}")
])

result = template.invoke({"input": "Explain the concept of langchain in a simple way."})
print(result)

