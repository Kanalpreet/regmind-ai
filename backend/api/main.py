from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import time

from backend.generation.generator import generate_response
from backend.retrieval.hybrid_search import hybrid_search
from backend.llm.conflict_detector import detect_conflict

from backend.memory.conversation_memory import (
    get_history,
    add_message
)

from backend.llm.question_rewriter import (
    rewrite_question
)

# =========================================
# FASTAPI APP
# =========================================

app = FastAPI(
    title="RegMind AI",
    description="AI Compliance Intelligence Platform",
    version="1.0"
)

# =========================================
# CORS
# =========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# =========================================
# REQUEST MODEL
# =========================================

class QueryRequest(BaseModel):
    session_id: str
    query: str


# =========================================
# ROOT
# =========================================

@app.get("/")
def home():

    return {
        "message": "🚀 RegMind AI Backend Running"
    }


# =========================================
# ASK AI
# =========================================

@app.post("/ask-ai")
def ask_ai(request: QueryRequest):

    # =====================================
    # START TIMER
    # =====================================

    start_time = time.time()

    # =====================================
    # LOAD CONVERSATION HISTORY
    # =====================================

    history = get_history(
        request.session_id
    )

    # =====================================
    # REWRITE QUESTION
    # =====================================

    rewritten_query = rewrite_question(
        history,
        request.query
    )

    # =====================================
    # HYBRID RETRIEVAL
    # =====================================

    retrieved_chunks = hybrid_search(
        rewritten_query
    )

    # =====================================
    # GENERATE RESPONSE
    # =====================================

    response = generate_response(
        request.query,
        retrieved_chunks,
        history
    )

    # =====================================
    # SAVE CONVERSATION
    # =====================================

    add_message(
        request.session_id,
        "user",
        request.query
    )

    add_message(
        request.session_id,
        "assistant",
        response["answer"]
    )

    # =====================================
    # METRICS
    # =====================================

    end_time = time.time()

    response["response_time"] = round(
        end_time - start_time,
        2
    )

    response["retrieved_chunks"] = len(
        retrieved_chunks
    )

    unique_documents = len({

        chunk.get("metadata", {}).get(
            "document_name",
            "Unknown"
        )

        for chunk in retrieved_chunks

    })

    response["source_documents"] = unique_documents

    response["retrieval_method"] = "Memory-Aware Hybrid RAG"

    response["vector_database"] = "Pinecone"

    response["model_accuracy"] = "70%"

    response["rewritten_query"] = rewritten_query

    return response


# =========================================
# CONFLICT DETECTION
# =========================================

@app.post("/detect-conflict")
def detect_compliance_conflict(
    request: QueryRequest
):

    result = detect_conflict(
        request.query
    )

    return result