# =========================================
# BUILD CONFLICT PROMPT
# =========================================

def build_conflict_prompt(
    query,
    rbi_chunks
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
    # FINAL PROMPT
    # =====================================

    prompt = f"""
You are RegMind AI, an expert Regulatory Compliance Conflict Detection Engine.

A compliance officer has submitted an INTERNAL BANK POLICY or operational scenario for review.

Your responsibility is to determine whether the submitted policy complies with the RBI regulations provided below.

=================================================
USER SUBMITTED POLICY
=================================================

{query}

=================================================
RELEVANT RBI REGULATIONS
=================================================

{rbi_context}

=================================================
TASK
=================================================

Compare ONLY the USER SUBMITTED POLICY with the RBI regulations.

DO NOT invent or assume any additional internal policies.

DO NOT compare against any retrieved internal policy.

A conflict exists ONLY if the submitted policy:

• Contradicts an RBI requirement.
• Omits a mandatory RBI obligation.
• Weakens or bypasses a mandatory RBI control.
• Allows something prohibited by RBI.

There is NO conflict if the submitted policy:

• Matches RBI requirements.
• Is stricter than RBI requirements.
• Adds additional internal controls that do not violate RBI regulations.

If there is insufficient information to conclude a conflict, return:

conflict_detected = false
risk_level = "Low"

=================================================
OUTPUT
=================================================

Return ONLY valid JSON.

{{
    "conflict_detected": true,
    "risk_level": "Low | Medium | High",
    "reason": "Brief explanation of why the policy conflicts or complies with RBI regulations.",
    "rbi_position": "Relevant RBI requirement.",
    "internal_policy_position": "Summarize ONLY the USER SUBMITTED POLICY.",
    "recommendation": "Action required to achieve compliance."
}}

Rules:

- Return ONLY JSON.
- No markdown.
- No explanations outside JSON.
- Do not hallucinate regulations.
- Do not fabricate internal policies.
- The value of "internal_policy_position" MUST summarize ONLY the USER SUBMITTED POLICY.
"""

    return prompt