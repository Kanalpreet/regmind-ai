from backend.ingest.pdf_parser import extract_text_from_pdf
from backend.ingest.chunker import chunk_documents
from backend.ingest.embedder import create_embeddings
from backend.ingest.pinecone_store import store_embeddings


def ingest_document(pdf_path, namespace):
    print("\n" + "=" * 50)
    print(f"📄 Ingesting: {pdf_path}")
    print(f"📂 Namespace: {namespace}")
    print("=" * 50)

    # Extract Text
    pages = extract_text_from_pdf(pdf_path)
    print(f"✅ Pages Extracted: {len(pages)}")

    # Chunk Documents
    chunks = chunk_documents(pages)
    print(f"✅ Chunks Created: {len(chunks)}")

    # Create Embeddings
    embedded_chunks = create_embeddings(chunks)
    print(f"✅ Embeddings Created: {len(embedded_chunks)}")

    # Store in Pinecone
    store_embeddings(
        embedded_chunks,
        namespace=namespace
    )

    print(f"🎉 Finished ingesting '{namespace}'")


if __name__ == "__main__":

    # RBI Regulations
    ingest_document(
        "data/raw/rbi_kyc.pdf",
        "rbi"
    )

    # Internal Policy
    ingest_document(
        "data/raw/internal_policy.pdf",
        "internal_policy"
    )

    print("\n" + "=" * 50)
    print("✅ RegMind AI Knowledge Base Rebuilt Successfully!")
    print("=" * 50)