from rank_bm25 import BM25Okapi

from backend.ingest.pdf_parser import extract_text_from_pdf

from backend.ingest.chunker import chunk_documents


# =========================================
# GLOBAL CACHE
# =========================================

bm25 = None

chunks = None


# =========================================
# INITIALIZE BM25 ONCE
# =========================================

def initialize_bm25():

    global bm25

    global chunks

    # Avoid rebuilding
    if bm25 is not None:

        return

    print("\n🚀 Initializing BM25 Retriever...\n")

    # =====================================
    # LOAD PDF
    # =====================================

    pdf_path = "data/raw/rbi_kyc.pdf"

    pages = extract_text_from_pdf(
        pdf_path
    )

    # =====================================
    # CHUNK DOCUMENTS
    # =====================================

    chunks = chunk_documents(
        pages
    )

    # =====================================
    # TOKENIZE
    # =====================================

    tokenized_chunks = [

        chunk["chunk_text"].split()

        for chunk in chunks
    ]

    # =====================================
    # CREATE BM25
    # =====================================

    bm25 = BM25Okapi(
        tokenized_chunks
    )

    print("✅ BM25 Ready")


# =========================================
# BM25 SEARCH
# =========================================

def bm25_search(

    query,

    top_k=5
):

    global bm25

    global chunks

    # =====================================
    # ENSURE INITIALIZED
    # =====================================

    if bm25 is None:

        initialize_bm25()

    # =====================================
    # TOKENIZE QUERY
    # =====================================

    tokenized_query = query.split()

    # =====================================
    # GET SCORES
    # =====================================

    scores = bm25.get_scores(
        tokenized_query
    )

    # =====================================
    # SORT RESULTS
    # =====================================

    ranked_results = sorted(

        enumerate(scores),

        key=lambda x: x[1],

        reverse=True
    )

    retrieved_chunks = []

    # =====================================
    # TOP K RESULTS
    # =====================================

    for idx, score in ranked_results[:top_k]:

        chunk_data = {

            "score": float(score),

            "chunk_text": chunks[idx]["chunk_text"],

            "metadata": {

                "document_name": chunks[idx]["document_name"],

                "page_number": chunks[idx]["page_number"],

                "topic": chunks[idx].get("topic"),

                "chunk_type": chunks[idx].get("chunk_type")
            }
        }

        retrieved_chunks.append(
            chunk_data
        )

    return retrieved_chunks