from backend.ml.predict_risk import predict_risk


sample_text = """
REs shall update customer KYC within 30 days.
Failure to comply may result in penalty.
"""

result = predict_risk(sample_text)

print("\n🚀 RISK PREDICTION:\n")

print(result)