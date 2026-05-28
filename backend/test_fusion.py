from backend.retrieval.fusion import reciprocal_rank_fusion


query = "What are RBI KYC requirements?"

results = reciprocal_rank_fusion(query)

print("\n🚀 HYBRID RAG RESULTS:\n")

for idx, chunk in enumerate(results):

    print(f"\nRESULT {idx + 1}")

    print(f"RRF Score: {chunk['rrf_score']}")

    print(f"Page: {chunk['page_number']}")

    print(f"Text: {chunk['chunk_text'][:300]}")