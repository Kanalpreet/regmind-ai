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

    # Predict encoded label
    prediction = model.predict(X)[0]

    # Decode label
    risk_label = str(

    encoder.inverse_transform(
        [prediction]
    )[0]
)

    return {

        "risk_level": risk_label,

        "features": features
    }