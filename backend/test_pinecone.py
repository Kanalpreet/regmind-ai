from ingest.pdf_parser import extract_text_from_pdf
from ingest.chunker import chunk_documents
from ingest.embedder import create_embeddings
from ingest.pinecone_store import store_embeddings


pdf_path = "data/raw/rbi_kyc.pdf"

# Extract text
pages = extract_text_from_pdf(pdf_path)

# Chunking
chunks = chunk_documents(pages)

# Embeddings
embedded_chunks = create_embeddings(chunks)

# Store in Pinecone
store_embeddings(

    embedded_chunks,

    namespace="rbi"
)