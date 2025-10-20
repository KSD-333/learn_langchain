from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader


loader = DirectoryLoader(path=".", glob="**/*.pdf", loader_cls=PyPDFLoader)
data = loader.load()

data2 = loader.lazy_load()

print(f"Loaded {len(data)} document(s)")

for i in data2:
    print(i.metadata)



for i in data:
    print(i.metadata)