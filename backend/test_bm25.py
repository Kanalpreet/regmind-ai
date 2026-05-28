from backend.retrieval.bm25_retriever import retrieve_bm25


query = "What are RBI KYC requirements?"

results = retrieve_bm25(query)

print("\n🔍 BM25 RESULTS:\n")

for idx, chunk in enumerate(results):

    print(f"\nRESULT {idx + 1}")

    print(f"Score: {chunk['score']}")

    print(f"Page: {chunk['page_number']}")

    print(f"Text: {chunk['chunk_text'][:300]}")