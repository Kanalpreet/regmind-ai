from backend.retrieval.vector_retriever import retrieve_chunks

from backend.retrieval.bm25_retriever import bm25_search

from backend.retrieval.fusion import reciprocal_rank_fusion


# =========================================
# HYBRID SEARCH
# =========================================

def hybrid_search(query):

    # =====================================
    # VECTOR RETRIEVAL (RBI NAMESPACE)
    # =====================================

    vector_results = retrieve_chunks(

        query=query,

        namespace="rbi"
    )

    # =====================================
    # BM25 RETRIEVAL
    # =====================================

    bm25_results = bm25_search(

        query
    )

    # =====================================
    # RECIPROCAL RANK FUSION
    # =====================================

    fused_results = reciprocal_rank_fusion(

        vector_results,

        bm25_results
    )

    return fused_results