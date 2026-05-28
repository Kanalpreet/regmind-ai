from backend.ingest.pdf_parser import extract_text_from_pdf
from backend.ingest.chunker import chunk_documents

pdf_path = "data/raw/rbi_kyc.pdf"

pages = extract_text_from_pdf(pdf_path)

chunks = chunk_documents(pages)

print(f"\n✅ Total Chunks Created: {len(chunks)}\n")

print("📄 FIRST CHUNK:\n")

print(chunks[0])