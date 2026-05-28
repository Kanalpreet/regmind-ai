# =========================================
# RECIPROCAL RANK FUSION (RRF)
# =========================================

def reciprocal_rank_fusion(

    vector_results,

    bm25_results,

    k=60
):

    fused_scores = {}

    # =====================================
    # VECTOR RESULTS
    # =====================================

    for rank, result in enumerate(vector_results):

        chunk_text = result["chunk_text"]

        score = 1 / (k + rank + 1)

        if chunk_text not in fused_scores:

            fused_scores[chunk_text] = {

                "score": 0,

                "data": result
            }

        fused_scores[chunk_text]["score"] += score

    # =====================================
    # BM25 RESULTS
    # =====================================

    for rank, result in enumerate(bm25_results):

        chunk_text = result["chunk_text"]

        score = 1 / (k + rank + 1)

        if chunk_text not in fused_scores:

            fused_scores[chunk_text] = {

                "score": 0,

                "data": result
            }

        fused_scores[chunk_text]["score"] += score

    # =====================================
    # SORT RESULTS
    # =====================================

    reranked_results = sorted(

        fused_scores.values(),

        key=lambda x: x["score"],

        reverse=True
    )

    # Final clean results
    final_results = [

        item["data"]

        for item in reranked_results
    ]

    return final_results