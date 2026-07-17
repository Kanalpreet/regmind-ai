import os
import json

from groq import Groq
from dotenv import load_dotenv

from backend.retrieval.dual_retriever import dual_retrieve

from backend.llm.conflict_prompt import build_conflict_prompt

from backend.config import GROQ_MODEL


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
# DETECT CONFLICT
# =========================================

def detect_conflict(

    query,

    top_k=5
):

    # =====================================
    # DUAL RETRIEVAL
    # =====================================

    retrieval_results = dual_retrieve(

        query,

        top_k=top_k,
        retrieve_internal=False
    )

    rbi_chunks = retrieval_results["rbi_chunks"]

   

    # =====================================
    # BUILD PROMPT
    # =====================================
    prompt = build_conflict_prompt(
    query,
    rbi_chunks
)

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

        temperature=0.1
    )

    llm_response = response.choices[0].message.content

    print("\n========== RAW GROQ RESPONSE ==========\n")
    print(llm_response)
    print("\n=======================================\n")

    # =====================================
    # PARSE JSON
    # =====================================

    try:

        parsed_response = json.loads(
            llm_response
        )

    except:

        parsed_response = {

            "conflict_detected": False,

            "risk_level": "Unknown",

            "reason": llm_response,

            "rbi_position": "",

            "internal_policy_position": "",

            "recommendation": "Parsing failed"
        }

    return parsed_response