# =========================================
# BUILD CONFLICT PROMPT
# =========================================

def build_conflict_prompt(

    query,

    rbi_chunks,

    internal_policy_chunks
):

    # =====================================
    # RBI CONTEXT
    # =====================================

    rbi_context = "\n\n".join(

        [
            chunk["chunk_text"]
            for chunk in rbi_chunks
        ]
    )

    # =====================================
    # INTERNAL POLICY CONTEXT
    # =====================================

    internal_context = "\n\n".join(

        [
            chunk["chunk_text"]
            for chunk in internal_policy_chunks
        ]
    )

    # =====================================
    # FINAL PROMPT
    # =====================================

    prompt = f"""
You are an AI compliance conflict detection engine.

Your task is to compare:

1. RBI regulatory requirements
2. Internal bank policy requirements

and identify whether there is any compliance conflict,
contradiction,
misalignment,
or operational risk.

USER QUERY:
{query}

=====================================
RBI REGULATION
=====================================

{rbi_context}

=====================================
INTERNAL POLICY
=====================================

{internal_context}

=====================================
TASK
=====================================

Analyze both carefully.

Return STRICTLY valid JSON.

FORMAT:

{{
    "conflict_detected": true or false,

    "risk_level": "Low | Medium | High",

    "reason": "...",

    "rbi_position": "...",

    "internal_policy_position": "...",

    "recommendation": "..."
}}

IMPORTANT:
- Return ONLY JSON
- No markdown
- No explanations outside JSON
"""

    return prompt