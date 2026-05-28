from backend.retrieval.vector_retriever import retrieve_chunks

from backend.retrieval.bm25_retriever import bm25_search

from backend.retrieval.fusion import reciprocal_rank_fusion


# =========================================
# HYBRID SEARCH
# =========================================

def hybrid_search(query):

    # Dense retrieval
    vector_results = retrieve_chunks(query)

    # BM25 retrieval
    bm25_results = bm25_search(query)

    # Fusion
    fused_results = reciprocal_rank_fusion(

        vector_results,

        bm25_results
    )

    return fused_results