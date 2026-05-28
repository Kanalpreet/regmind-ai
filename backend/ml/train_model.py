import os
import pandas as pd
import joblib

from xgboost import XGBClassifier

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from risk_features import extract_risk_features
from training_data import training_examples


# =========================================
# PROJECT ROOT PATH
# =========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

# =========================================
# MODELS DIRECTORY
# =========================================

MODELS_DIR = os.path.join(
    BASE_DIR,
    "models"
)

# Create models folder if not exists
os.makedirs(MODELS_DIR, exist_ok=True)

# =========================================
# BUILD DATASET
# =========================================

feature_rows = []
labels = []

for example in training_examples:

    # Extract ML features
    features = extract_risk_features(
        example["text"]
    )

    feature_rows.append(features)

    labels.append(example["risk"])

# =========================================
# FEATURE MATRIX
# =========================================

X = pd.DataFrame(feature_rows)

# =========================================
# LABEL ENCODING
# =========================================

encoder = LabelEncoder()

y = encoder.fit_transform(labels)

# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42
)

# =========================================
# XGBOOST MODEL
# =========================================

model = XGBClassifier(

    n_estimators=50,

    max_depth=3,

    learning_rate=0.1,

    objective="multi:softmax",

    eval_metric="mlogloss"
)

# Train model
model.fit(X_train, y_train)

# =========================================
# EVALUATION
# =========================================

predictions = model.predict(X_test)

print("\n🚀 CLASSIFICATION REPORT:\n")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)

# =========================================
# SAVE MODEL
# =========================================

MODEL_PATH = os.path.join(
    MODELS_DIR,
    "xgboost_risk.pkl"
)

ENCODER_PATH = os.path.join(
    MODELS_DIR,
    "label_encoder.pkl"
)

# Save trained model
joblib.dump(
    model,
    MODEL_PATH
)

# Save label encoder
joblib.dump(
    encoder,
    ENCODER_PATH
)

print("\n✅ Risk Model Saved Successfully")

print(f"\n📁 Model Path: {MODEL_PATH}")

print(f"📁 Encoder Path: {ENCODER_PATH}")