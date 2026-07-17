import os
import joblib
import pandas as pd

from backend.ml.risk_features import extract_risk_features


# =========================================
# PROJECT ROOT
# =========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

# =========================================
# MODEL PATHS
# =========================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "xgboost_risk.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "label_encoder.pkl"
)

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load(MODEL_PATH)

encoder = joblib.load(ENCODER_PATH)

print("\n✅ Risk Model Loaded Successfully")


# =========================================
# PREDICT RISK
# =========================================

def predict_risk(text):

    # Extract ML features
    features = extract_risk_features(text)

    # Convert into DataFrame
    X = pd.DataFrame([features])

    # Predict risk class
    prediction = model.predict(X)[0]

    # Predict confidence
    probabilities = model.predict_proba(X)[0]

    confidence = round(max(probabilities) * 100, 2)

    # Decode label
    risk_label = encoder.inverse_transform([prediction])[0]

    # Human-readable risk factors
    risk_factors = []

    if features.get("has_shall"):
        risk_factors.append("Mandatory compliance clause detected")

    if features.get("has_must"):
        risk_factors.append("Mandatory obligation detected")

    if features.get("has_deadline"):
        risk_factors.append("Compliance deadline mentioned")

    if features.get("has_penalty"):
        risk_factors.append("Penalty provision detected")

    if features.get("has_violation"):
        risk_factors.append("Violation clause detected")

    if features.get("has_customer_data"):
        risk_factors.append("Customer data involved")

    return {
        "risk_level": risk_label,
        "confidence": confidence,
        "risk_factors": risk_factors
    }