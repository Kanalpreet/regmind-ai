from backend.retrieval.hybrid_search import hybrid_search

from backend.generation.generator import generate_response


query = "What are RBI KYC compliance requirements?"


# =====================================
# RETRIEVE
# =====================================

results = hybrid_search(query)


# =====================================
# GENERATE RESPONSE
# =====================================

response = generate_response(

    query,
    results
)

print("\n🚀 FINAL INTEGRATED AI RESPONSE:\n")

print(response)