from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts = PyMuPDFLoader("Practice Questions.pdf")
documents = texts.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
documents = text_splitter.split_documents(documents)

vector_db = Chroma.from_documents(documents, embedding=embedding_model)

query = input("Enter your query: ")
results = vector_db.similarity_search(query, k=1)
for r in results:
    print(r.page_content)