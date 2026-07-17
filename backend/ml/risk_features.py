import re

def extract_risk_features(text):

    text_lower = text.lower()

    features = {

        # Regulatory obligation
        "has_shall": int("shall" in text_lower),
        "has_must": int("must" in text_lower),
        "has_required": int("required" in text_lower),
        "has_mandatory": int("mandatory" in text_lower),

        # Enforcement
        "has_penalty": int("penalty" in text_lower),
        "has_violation": int("violation" in text_lower),
        "has_fine": int("fine" in text_lower),
        "has_non_compliance": int("non-compliance" in text_lower),

        # Time urgency
        "has_deadline": int(
            bool(
                re.search(
                    r"\d+\s*(day|days|month|months|year|years)",
                    text_lower
                )
            )
        ),

        # Sensitive domains
        "has_customer_data": int(
            any(
                word in text_lower
                for word in [
                    "customer",
                    "kyc",
                    "account",
                    "personal data",
                    "identity"
                ]
            )
        ),

        "has_reporting": int(
            any(
                word in text_lower
                for word in [
                    "report",
                    "reporting",
                    "submit"
                ]
            )
        ),

        "has_rbi_reference": int(
            "rbi" in text_lower
        ),

        "has_bank_reference": int(
            "bank" in text_lower
        ),

        "has_confidentiality": int(
            any(
                word in text_lower
                for word in [
                    "confidential",
                    "privacy",
                    "confidentiality"
                ]
            )
        ),

        # Complexity
        "word_count": len(text.split()),

        "text_length": len(text),

        "numeric_count": len(re.findall(r"\d+", text))
    }

    return features