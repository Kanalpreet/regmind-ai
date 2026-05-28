import os
import json

from groq import Groq
from dotenv import load_dotenv

from backend.config import GROQ_MODEL

from backend.ml.predict_risk import predict_risk


# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# GROQ CLIENT
# =========================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================================
# GENERATE RESPONSE
# =========================================

def generate_response(query, retrieved_chunks):

    # =====================================
    # BUILD CONTEXT
    # =====================================

    context = "\n\n".join(

        [
            chunk["chunk_text"]
            for chunk in retrieved_chunks
        ]
    )

    # =====================================
    # COMBINE TEXT FOR RISK ANALYSIS
    # =====================================

    combined_text = " ".join(

        [
            chunk["chunk_text"]
            for chunk in retrieved_chunks
        ]
    )

    # =====================================
    # ML RISK PREDICTION
    # =====================================

    risk_result = predict_risk(
        combined_text
    )

    # =====================================
    # SOURCE PAGES
    # =====================================

    source_pages = list(

    set(

        [

            chunk.get(
                "metadata",
                {}
            ).get(
                "page_number",

                chunk.get("page_number")
            )

            for chunk in retrieved_chunks
        ]
    )
)

    # =====================================
    # PROMPT
    # =====================================

    prompt = f"""
You are an RBI compliance AI assistant.

Answer ONLY using the provided context.

Risk analysis from ML engine:
{risk_result['risk_level']}

CONTEXT:
{context}

QUESTION:
{query}

Return STRICTLY valid JSON:

{{
  "answer": "...",

  "compliance_points": [
    "...",
    "..."
  ],

  "summary": "..."
}}
"""

    # =====================================
    # GROQ RESPONSE
    # =====================================

    response = client.chat.completions.create(

        model=GROQ_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    # =====================================
    # PARSE LLM JSON
    # =====================================

    llm_response = response.choices[0].message.content

    try:

        parsed_response = json.loads(
            llm_response
        )

    except:

        parsed_response = {

            "answer": llm_response,

            "compliance_points": [],

            "summary": "Parsing failed"
        }

    # =====================================
    # FINAL RESPONSE
    # =====================================

    final_response = {

        "answer": parsed_response.get(
            "answer"
        ),

        "compliance_points": parsed_response.get(
            "compliance_points"
        ),

        "summary": parsed_response.get(
            "summary"
        ),

        # ML OUTPUT
        "risk_analysis": risk_result,

        # SOURCE TRACEABILITY
        "source_pages": source_pages
    }

    return final_response
