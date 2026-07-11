from backend.retrieval.vector_retriever import retrieve_chunks


# =========================================
# DUAL RETRIEVAL
# =========================================

def dual_retrieve(

    query,

    top_k=5
):

    # =====================================
    # RBI RETRIEVAL
    # =====================================

    rbi_chunks = retrieve_chunks(

        query,

        namespace="rbi",

        top_k=top_k
    )

    # =====================================
    # INTERNAL POLICY RETRIEVAL
    # =====================================

    internal_policy_chunks = retrieve_chunks(

        query,

        namespace="internal_policy",

        top_k=top_k
    )


    print("\n========== RBI ==========")
    print(rbi_chunks)

    print("\n========== INTERNAL ==========")
    print(internal_policy_chunks)

    return {

        "rbi_chunks": rbi_chunks,

        "internal_policy_chunks": internal_policy_chunks
    }