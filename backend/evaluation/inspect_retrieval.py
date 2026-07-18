from backend.retrieval.vector_retriever import retrieve_chunks

TEST_CASES = [

    {
        "id": "C02",
        "query": "For companies, beneficial ownership shall be determined using a 10% ownership threshold."
    },

    {
        "id": "C03",
        "query": "For partnership firms, beneficial ownership shall be determined using a 10% ownership threshold."
    },

    {
        "id": "C04",
        "query": "For trusts, beneficial ownership shall be determined using a 15% ownership threshold."
    },

    {
        "id": "C05",
        "query": "For unincorporated associations, beneficial ownership shall be determined using a 10% ownership threshold."
    },

    {
        "id": "C06",
        "query": "High-risk customer accounts shall be reviewed every three months."
    }

]

for case in TEST_CASES:

    print("\n")
    print("=" * 80)
    print(f"TEST CASE : {case['id']}")
    print("=" * 80)

    retrieve_chunks(
        query=case["query"],
        namespace="rbi",
        top_k=5
    )