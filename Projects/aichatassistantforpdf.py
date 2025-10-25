from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
loader = PyMuPDFLoader("ISE 1 Topics.pdf")
documents = loader.load()


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


vectorstore = Chroma.from_documents(documents, embedding=embeddings)


retriever = vectorstore.as_retriever(search_kwargs={"k": 2})


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


qa_chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gemini-2.0-flash-exp"),
    retriever=retriever,
    memory=memory,
    verbose=True
)


print("AI Document Assistant Ready!\n")
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = qa_chain.invoke({"question": query})
    print("AI:", response["answer"])
