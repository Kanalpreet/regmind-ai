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
You are an AI Regulatory Compliance Conflict Detection Engine.

A user has submitted an internal bank policy or operational scenario.

Your task is to compare the USER'S POLICY against the RBI regulations provided below.

Determine whether the submitted policy:
- contradicts RBI regulations,
- omits mandatory RBI requirements,
- weakens regulatory obligations,
- or is fully compliant.

========================
USER SUBMITTED POLICY
========================

{query}

========================
RELEVANT RBI REGULATIONS
========================

{rbi_context}

========================
TASK
========================

Compare ONLY the user submitted policy with the RBI regulations.

Do NOT compare the retrieved internal policy.

If the user policy follows RBI requirements, return:

conflict_detected = false
risk_level = "Low"

Only report a conflict when there is a genuine contradiction or missing mandatory RBI requirement.

Return STRICT JSON only.

{{
    "conflict_detected": true,
    "risk_level": "Low | Medium | High",
    "reason": "...",
    "rbi_position": "...",
    "internal_policy_position": "...",
    "recommendation": "..."
}}
"""
    
    return prompt