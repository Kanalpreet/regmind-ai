from backend.retrieval.dual_retriever import dual_retrieve


query = "What are KYC updation requirements?"


results = dual_retrieve(query)


print("\n🚀 RBI RESULTS:\n")

for chunk in results["rbi_chunks"]:

    print(chunk)

    print("\n------------------\n")


print("\n🚀 INTERNAL POLICY RESULTS:\n")

for chunk in results["internal_policy_chunks"]:

    print(chunk)

    print("\n------------------\n")