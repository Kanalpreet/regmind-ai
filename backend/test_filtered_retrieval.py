from backend.retrieval.vector_retriever import retrieve_chunks


query = "What are RBI KYC requirements?"

results = retrieve_chunks(

    query=query,

    top_k=5,

    topic_filter="KYC"
)

print("\n🚀 FILTERED RETRIEVAL RESULTS:\n")

for idx, chunk in enumerate(results):

    print(f"\nRESULT {idx + 1}")

    print(f"Score: {chunk['score']}")

    print(f"Topic: {chunk['topic']}")

    print(f"Chunk Type: {chunk['chunk_type']}")

    print(f"Page: {chunk['page_number']}")

    print(f"Text: {chunk['chunk_text'][:300]}")