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
You are RegMind AI, an expert Regulatory Compliance Conflict Detection Engine specializing in RBI banking regulations.

A compliance officer has submitted an internal bank policy or operational scenario.

Your task is to determine whether the submitted policy CONFLICTS with the RBI regulations provided below.

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

Compare ONLY the USER SUBMITTED POLICY against the RBI regulations.

DO NOT invent additional internal policies.

DO NOT assume the submitted policy is a complete Standard Operating Procedure (SOP).

Treat the submitted text as an isolated policy statement unless it explicitly claims to be a complete policy.

=================================================
DECISION RULES
=================================================

Return conflict_detected = true ONLY if the submitted policy:

• Explicitly contradicts an RBI regulation.
• Permits an activity prohibited by RBI.
• Weakens or bypasses a mandatory RBI control.
• Explicitly states something inconsistent with RBI requirements.

Return conflict_detected = false if the submitted policy:

• Is consistent with RBI regulations.
• Is a short summary of RBI requirements.
• Does not mention every RBI requirement.
• Is stricter than RBI regulations.
• Adds additional internal controls without violating RBI regulations.
• Does not provide enough information to conclude a contradiction.

IMPORTANT:

Do NOT treat a policy as conflicting simply because it does not mention every RBI requirement.

Missing unrelated RBI clauses are NOT conflicts.

Only identify a conflict when there is a clear contradiction between the submitted policy and the RBI regulations.

=================================================
OUTPUT
=================================================

Return ONLY valid JSON.

{{
    "conflict_detected": true,
    "risk_level": "Low | Medium | High",
    "reason": "Explain why the submitted policy conflicts with or complies with the RBI regulation.",
    "rbi_position": "Relevant RBI requirement used for comparison.",
    "internal_policy_position": "Summarize ONLY the USER SUBMITTED POLICY.",
    "recommendation": "Recommended action."
}}

=================================================
RULES
=================================================

- Return ONLY JSON.
- Do NOT use markdown.
- Do NOT fabricate RBI regulations.
- Do NOT fabricate internal policies.
- Base your decision ONLY on the submitted policy and the retrieved RBI regulations.
- If there is no explicit contradiction, set:
  - conflict_detected = false
  - risk_level = "Low"
"""

    return prompt