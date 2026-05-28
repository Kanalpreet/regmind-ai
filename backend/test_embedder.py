from ingest.pdf_parser import extract_text_from_pdf
from ingest.chunker import chunk_documents
from ingest.embedder import create_embeddings

pdf_path = "data/raw/rbi_kyc.pdf"

# Extract pages
pages = extract_text_from_pdf(pdf_path)

# Create chunks
chunks = chunk_documents(pages)

# Create embeddings
embedded_chunks = create_embeddings(chunks)

print(f"\n✅ Total Embedded Chunks: {len(embedded_chunks)}\n")

print("📄 FIRST EMBEDDED CHUNK:\n")

print(embedded_chunks[0].keys())

print("\n📏 Embedding Dimension:\n")

print(len(embedded_chunks[0]["embedding"]))