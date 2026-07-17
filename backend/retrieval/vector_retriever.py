import os

from pinecone import Pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from backend.config import (
    PINECONE_INDEX,
    EMBEDDING_MODEL
)

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# INITIALIZE PINECONE
# =========================================

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

# =========================================
# CONNECT INDEX
# =========================================

index = pc.Index(
    PINECONE_INDEX
)

# =========================================
# LOAD EMBEDDING MODEL
# =========================================

model = SentenceTransformer(
    EMBEDDING_MODEL,
    local_files_only=True
)

# =========================================
# RETRIEVE CHUNKS
# =========================================

def retrieve_chunks(
    query,
    namespace,
    top_k=5,
    topic_filter=None,
    chunk_type_filter=None
):

    print("\n========================================")
    print("QUERY")
    print(query)
    print("========================================\n")

    # =====================================
    # QUERY EMBEDDING
    # =====================================

    query_embedding = model.encode(query).tolist()

    # =====================================
    # METADATA FILTER
    # =====================================

    metadata_filter = {}

    if topic_filter:
        metadata_filter["topic"] = topic_filter

    if chunk_type_filter:
        metadata_filter["chunk_type"] = chunk_type_filter

    # =====================================
    # PINECONE QUERY
    # =====================================

    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        namespace=namespace,
        include_metadata=True,
        filter=metadata_filter if metadata_filter else None
    )

    # =====================================
    # FORMAT RESULTS
    # =====================================

    retrieved_chunks = []

    for match in results["matches"]:

        chunk_data = {

            "score": float(match["score"]),

            "chunk_text": match["metadata"]["chunk_text"],

            "metadata": {

                "document_name": match["metadata"]["document_name"],

                "page_number": match["metadata"]["page_number"],

                "topic": match["metadata"].get("topic"),

                "chunk_type": match["metadata"].get("chunk_type"),

                "namespace": namespace
            }
        }

        retrieved_chunks.append(chunk_data)

    # =====================================
    # DEBUG OUTPUT
    # =====================================

    print("\n========================================")
    print(f"Namespace : {namespace}")
    print(f"Retrieved : {len(retrieved_chunks)} chunks")
    print("========================================")

    for i, chunk in enumerate(retrieved_chunks):

        print(f"\n-------- RESULT {i+1} --------")

        print(f"Similarity Score : {chunk['score']:.4f}")

        print(f"Document         : {chunk['metadata']['document_name']}")

        print(f"Page             : {chunk['metadata']['page_number']}")

        if chunk["metadata"]["topic"]:
            print(f"Topic            : {chunk['metadata']['topic']}")

        if chunk["metadata"]["chunk_type"]:
            print(f"Chunk Type       : {chunk['metadata']['chunk_type']}")

        print("\nChunk Text:\n")

        print(chunk["chunk_text"])

        print("\n----------------------------------------")

    print("\n========================================\n")

    return retrieved_chunks