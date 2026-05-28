import re


def extract_risk_features(text):

    text_lower = text.lower()

    features = {

        # Compliance obligation
        "has_shall": int(
            "shall" in text_lower
        ),

        "has_must": int(
            "must" in text_lower
        ),

        # Penalty indicators
        "has_penalty": int(
            "penalty" in text_lower
        ),

        "has_violation": int(
            "violation" in text_lower
        ),

        "has_fine": int(
            "fine" in text_lower
        ),

        # Time urgency
        "has_deadline": int(
            bool(
                re.search(
                    r"\d+\s*(days|months|years)",
                    text_lower
                )
            )
        ),

        # Sensitive financial keywords
        "has_customer_data": int(
            "customer" in text_lower
            or
            "kyc" in text_lower
        ),

        # Chunk complexity
        "text_length": len(text)
    }

    return features