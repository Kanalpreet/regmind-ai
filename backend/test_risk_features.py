from backend.ml.risk_features import extract_risk_features


sample_text = """
REs shall update customer KYC within 30 days.
Failure may result in penalty and regulatory action.
"""

features = extract_risk_features(sample_text)

print("\n🚀 EXTRACTED RISK FEATURES:\n")

for key, value in features.items():

    print(f"{key}: {value}")