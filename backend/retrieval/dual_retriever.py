from backend.retrieval.vector_retriever import retrieve_chunks


# =========================================
# RETRIEVE CONTEXT
# =========================================

def dual_retrieve(
    query,
    top_k=5,
    retrieve_internal=True
):

    # =====================================
    # RBI RETRIEVAL
    # =====================================

    rbi_chunks = retrieve_chunks(
        query,
        namespace="rbi",
        top_k=top_k
    )

    internal_policy_chunks = []

    # =====================================
    # INTERNAL POLICY RETRIEVAL (OPTIONAL)
    # =====================================

    if retrieve_internal:

        internal_policy_chunks = retrieve_chunks(
            query,
            namespace="internal_policy",
            top_k=top_k
        )

    print("\n========== RBI ==========")
    print(rbi_chunks)

    if retrieve_internal:
        print("\n========== INTERNAL ==========")
        print(internal_policy_chunks)

    return {

        "rbi_chunks": rbi_chunks,

        "internal_policy_chunks": internal_policy_chunks
    }