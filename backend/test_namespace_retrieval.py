from backend.retrieval.vector_retriever import retrieve_chunks


query = "What are RBI KYC compliance requirements?"


# =====================================
# RBI RETRIEVAL
# =====================================

rbi_results = retrieve_chunks(

    query,

    namespace="rbi"
)

print("\n🚀 RBI RESULTS:\n")

for chunk in rbi_results:

    print(chunk)

    print("\n-----------------\n")


# =====================================
# INTERNAL POLICY RETRIEVAL
# =====================================

policy_results = retrieve_chunks(

    query,

    namespace="internal_policy"
)

print("\n🚀 INTERNAL POLICY RESULTS:\n")

for chunk in policy_results:

    print(chunk)

    print("\n-----------------\n")