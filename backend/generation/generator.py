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

def generate_response(
    query,
    retrieved_chunks,
    conversation_history
):

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
    # COMBINE TEXT FOR ML
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
                chunk.get("metadata", {}).get(
                    "page_number",
                    chunk.get("page_number")
                )
                for chunk in retrieved_chunks
            ]
        )
    )

    # =====================================
    # CONVERSATION HISTORY
    # =====================================

    history = ""

    for message in conversation_history:

        history += (
            f"{message['role'].capitalize()}: "
            f"{message['content']}\n"
        )

    # =====================================
    # PROMPT
    # =====================================

    prompt = f"""
You are RegMind AI, an expert RBI Compliance AI Assistant.

Answer ONLY using the retrieved RBI regulations.

You may use the previous conversation ONLY for understanding context.

Do NOT invent RBI regulations.

If the answer is not available in the retrieved context, clearly say so.

=================================================
CONVERSATION HISTORY
=================================================

{history}

=================================================
ML RISK ANALYSIS
=================================================

Predicted Risk Level:
{risk_result['risk_level']}

=================================================
RETRIEVED RBI CONTEXT
=================================================

{context}

=================================================
CURRENT USER QUESTION
=================================================

{query}

=================================================
OUTPUT
=================================================

Return STRICTLY valid JSON.

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
    # PARSE JSON
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
    # SOURCE EVIDENCE
    # =====================================

    source_evidence = []

    seen = set()

    for chunk in retrieved_chunks:

        metadata = chunk.get("metadata", {})

        document = metadata.get(
            "document_name",
            "Unknown Document"
        )

        document = (
            document
            .replace(".pdf", "")
            .replace("_", " ")
            .title()
        )

        page = metadata.get(
            "page_number",
            "-"
        )

        source = metadata.get(
            "namespace",
            "Unknown"
        )

        key = (
            document,
            page,
            source
        )

        if key not in seen:

            seen.add(key)

            source_evidence.append({

                "document": document,

                "page": page,

                "source": source
            })

    # =====================================
    # FINAL RESPONSE
    # =====================================

    return {

        "answer": parsed_response.get(
            "answer"
        ),

        "compliance_points": parsed_response.get(
            "compliance_points"
        ),

        "summary": parsed_response.get(
            "summary"
        ),

        "risk_analysis": risk_result,

        "source_pages": source_pages,

        "source_evidence": source_evidence
    }