from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma, FAISS
from dotenv import load_dotenv
load_dotenv()


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


texts = [
    "Satellite remote sensing helps monitor land cover changes.",
    "Agentic AI enables autonomous decision making.",
    "LangChain allows developers to build AI agents easily."
]


vector_db = Chroma.from_texts(texts, embedding=embedding_model)
faiss_db = FAISS.from_texts(texts, embedding=embedding_model)

query = "What is LangChain used for?"
results = vector_db.similarity_search(query, k=1)

for r in results:
    print(r.page_content)

print("="*40)

query2 = "What is use of satellite remote sensing?"
faiss_results = faiss_db.similarity_search(query2, k=1)

for r in faiss_results:
    print(r.page_content)
