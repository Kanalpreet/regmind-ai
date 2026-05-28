import os

from pinecone import Pinecone
from dotenv import load_dotenv

from backend.config import PINECONE_INDEX


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
# STORE EMBEDDINGS
# =========================================

def store_embeddings(

    embedded_chunks,

    namespace
):

    batch_size = 20

    vectors = []

    # =====================================
    # PREPARE VECTORS
    # =====================================

    for idx, chunk in enumerate(embedded_chunks):

        vector = {

            "id": f"{namespace}_{idx}",

            "values": chunk["embedding"],

            "metadata": {

                "document_name": chunk["document_name"],

                "page_number": chunk["page_number"],

                "chunk_text": chunk["chunk_text"],

                "topic": chunk["topic"],

                "chunk_type": chunk["chunk_type"],

                # VERY IMPORTANT
                "namespace": namespace
            }
        }

        vectors.append(vector)

    # =====================================
    # UPSERT IN BATCHES
    # =====================================

    for i in range(0, len(vectors), batch_size):

        batch = vectors[i:i + batch_size]

        index.upsert(

            vectors=batch,

            namespace=namespace
        )

        print(
            f"✅ Uploaded batch {i // batch_size + 1}"
        )

    print(
        f"\n🎉 Total vectors stored in '{namespace}': {len(vectors)}"
    )