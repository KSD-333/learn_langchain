from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k=5
)

query = "Explain the geopolitical of india and china border dispute"

results = retriever.invoke(query)

for i, result in enumerate(results):
    print(f"Result {i+1}\nContent: {result.page_content}\n")