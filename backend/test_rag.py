from rag.retriever import retrieve_context

query = "power rule derivative"

results = retrieve_context(query)

print("\nRetrieved Context:\n")

for r in results:
    print(r)