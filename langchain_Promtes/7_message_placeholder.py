from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

chat_history = []

with open('chat_history.txt') as file:
        chat_history.extend(file.readlines())


result = template.invoke({"chat_history": chat_history, "input": "Explain the concept of langchain in a simple way."})


print(chat_history)