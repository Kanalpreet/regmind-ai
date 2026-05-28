from sentence_transformers import SentenceTransformer

from backend.config import EMBEDDING_MODEL

# Load locally only
model = SentenceTransformer(
    EMBEDDING_MODEL,
    local_files_only=True
)


def create_embeddings(chunks):

    embedded_chunks = []

    for chunk in chunks:

        text = chunk["chunk_text"]

        embedding = model.encode(text).tolist()

        chunk_data = {

            "document_name": chunk["document_name"],

            "page_number": chunk["page_number"],

            "chunk_text": text,

            "embedding": embedding,

            # PASS METADATA FORWARD
            "topic": chunk["topic"],

            "chunk_type": chunk["chunk_type"]
        }

        # MUST BE INSIDE LOOP
        embedded_chunks.append(chunk_data)

    # MUST BE OUTSIDE LOOP
    return embedded_chunks