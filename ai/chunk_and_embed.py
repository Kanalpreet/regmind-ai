from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pdf_reader import extract_text


# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks


def create_embeddings(chunks):
    embeddings = model.encode(chunks)
    return np.array(embeddings)


def store_in_faiss(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index


if __name__ == "__main__":
    print("\n📄 Reading and processing PDF...\n")

    text = extract_text("data/raw/rbi_kyc.pdf")

    chunks = chunk_text(text)

    print(f"✅ Total Chunks Created: {len(chunks)}")

    embeddings = create_embeddings(chunks)

    print("✅ Embeddings Created")

    index = store_in_faiss(embeddings)

    print("✅ Stored in FAISS Vector DB")

    # Test search
    query = "What is KYC?"
    query_embedding = model.encode([query])

    D, I = index.search(query_embedding, k=3)

    print("\n🔍 Top Relevant Chunks:\n")

    for i in I[0]:
        print(chunks[i])
        print("\n---\n")