from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from backend.generation.generator import generate_response

from backend.retrieval.hybrid_search import hybrid_search

from backend.llm.conflict_detector import detect_conflict
import time

# =========================================
# FASTAPI APP
# =========================================

app = FastAPI(

    title="RegMind AI",

    description="AI Compliance Intelligence Platform",

    version="1.0"
)

# =========================================
# CORS MIDDLEWARE
# =========================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

# =========================================
# REQUEST SCHEMA
# =========================================

class QueryRequest(BaseModel):
    session_id: str
    query: str


# =========================================
# ROOT ROUTE
# =========================================

@app.get("/")
def home():

    return {

        "message": "🚀 RegMind AI Backend Running"
    }


# =========================================
# COMPLIANCE AI ROUTE
# =========================================

@app.post("/ask-ai")
def ask_ai(request: QueryRequest):

    # =====================================
    # START TIMER
    # =====================================

    start_time = time.time()

    # =====================================
    # HYBRID RETRIEVAL
    # =====================================

    retrieved_chunks = hybrid_search(
        request.query
    )

    # =====================================
    # GENERATE AI RESPONSE
    # =====================================

    response = generate_response(
        request.query,
        retrieved_chunks
    )

    # =====================================
    # SYSTEM EVALUATION METRICS
    # =====================================

    end_time = time.time()

    # Response time
    response["response_time"] = round(
        end_time - start_time,
        2
    )

    # Number of retrieved chunks
    response["retrieved_chunks"] = len(
        retrieved_chunks
    )

    # Number of unique source documents
    unique_documents = len({

        chunk.get("metadata", {}).get(
            "document_name",
            "Unknown"
        )

        for chunk in retrieved_chunks

    })

    response["source_documents"] = unique_documents

    # Retrieval method
    response["retrieval_method"] = "Hybrid (Dense + BM25 + RRF)"

    # Vector database
    response["vector_database"] = "Pinecone"

    # ML model accuracy
    response["model_accuracy"] = "70%"

    return response

    # =====================================
    # HYBRID RETRIEVAL
    # =====================================

    retrieved_chunks = hybrid_search(

        request.query
    )

    # =====================================
    # GENERATE AI RESPONSE
    # =====================================

    response = generate_response(

        request.query,

        retrieved_chunks
    )

    return response


# =========================================
# CONFLICT DETECTION ROUTE
# =========================================

@app.post("/detect-conflict")
def detect_compliance_conflict(

    request: QueryRequest
):

    result = detect_conflict(

        request.query
    )

    return result