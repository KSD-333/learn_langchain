from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders import python

loader = python.PythonLoader("Ex_prompt_json.py")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, chunk_size=100, chunk_overlap=20)
docs = text_splitter.split_documents(documents)


print(len(docs))
print(docs[0].page_content)