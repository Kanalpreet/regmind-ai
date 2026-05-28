from backend.retrieval.fusion import reciprocal_rank_fusion
from backend.generation.generator import generate_response


query = "What are RBI KYC requirements?"

# Retrieve relevant chunks
retrieved_chunks = reciprocal_rank_fusion(query)

# Generate response
response = generate_response(
    query,
    retrieved_chunks
)

print("\n🚀 FINAL AI RESPONSE:\n")

print(response)