from backend.retrieval.hybrid_search import hybrid_search

query = "Video KYC"

results = hybrid_search(
    query=query,
    namespace="rbi"
)

print(results)