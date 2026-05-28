from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from backend.generation.generator import generate_response

from backend.retrieval.hybrid_search import hybrid_search

from backend.llm.conflict_detector import detect_conflict


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
def ask_ai(

    request: QueryRequest
):

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