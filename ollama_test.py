# minimal_ollama.py
from langchain_ollama import ChatOllama

# Point to the local Ollama endpoint (default is localhost:11434)
ollama_host = "http://localhost:11434"

llm = ChatOllama(
    model="llama3.2:latest",         
    base_url=ollama_host,      
    temperature=0.2,           
)
while(True):
    Chat = input("Enter Text For Answer: ")
    if Chat.lower() in ['bye', 'exit', 'quit']: 
        print("Goodbye!")
        break
    else:
        response = llm.invoke(Chat)
        print("<---Result--->")
        print(response.content)  # `.content` holds the raw string