# backend/config.py

# =========================
# CHUNKING CONFIG
# =========================

CHUNK_SIZE = 900
CHUNK_OVERLAP = 150
# Pinecone

PINECONE_INDEX = "regmind-ai"
# =========================
# COLLECTIONS
# =========================
GROQ_MODEL = "llama-3.1-8b-instant"
REGULATION_COLLECTION = "external_regulations"
POLICY_COLLECTION = "internal_policies"

# =========================
# EMBEDDING MODEL
# =========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"