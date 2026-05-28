from ingest.pdf_parser import extract_text_from_pdf

from ingest.chunker import chunk_documents

from ingest.embedder import create_embeddings

from ingest.pinecone_store import store_embeddings


# =====================================
# PDF PATH
# =====================================

pdf_path = "data/raw/internal_policy.pdf"

# =====================================
# EXTRACT TEXT
# =====================================

pages = extract_text_from_pdf(
    pdf_path
)

print(f"\n✅ Pages Extracted: {len(pages)}")

# =====================================
# CHUNK DOCUMENTS
# =====================================

chunks = chunk_documents(
    pages
)

print(f"\n✅ Chunks Created: {len(chunks)}")

# =====================================
# CREATE EMBEDDINGS
# =====================================

embedded_chunks = create_embeddings(
    chunks
)

print(f"\n✅ Embeddings Created: {len(embedded_chunks)}")

# =====================================
# STORE IN PINECONE
# =====================================

store_embeddings(

    embedded_chunks,

    namespace="internal_policy"
)