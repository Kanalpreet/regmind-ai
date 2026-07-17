import os
import joblib
import pandas as pd

from xgboost import XGBClassifier

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    confusion_matrix
)

from risk_features import extract_risk_features
from training_data import training_examples


# =========================================
# PROJECT ROOT
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

os.makedirs(MODELS_DIR, exist_ok=True)

# =========================================
# BUILD DATASET
# =========================================

feature_rows = []
labels = []

for example in training_examples:

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

    test_size=0.20,

    random_state=42,

    stratify=y

)

# =========================================
# XGBOOST MODEL
# =========================================

model = XGBClassifier(

    n_estimators=150,

    max_depth=4,

    learning_rate=0.1,

    objective="multi:softprob",

    eval_metric="mlogloss",

    random_state=42

)

# =========================================
# TRAIN MODEL
# =========================================

model.fit(

    X_train,
    y_train

)

# =========================================
# PREDICTIONS
# =========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

# =========================================
# EVALUATION
# =========================================

print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print(f"\nAccuracy : {accuracy:.2%}\n")

print(classification_report(

    y_test,

    predictions,

    target_names=encoder.classes_,

    zero_division=0

))

print("Confusion Matrix\n")

print(

    confusion_matrix(
        y_test,
        predictions
    )

)

# =========================================
# FEATURE IMPORTANCE
# =========================================

importance_df = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})

importance_df = importance_df.sort_values(

    by="Importance",

    ascending=False

)

print("\n" + "=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

print(importance_df)

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

joblib.dump(

    model,

    MODEL_PATH

)

joblib.dump(

    encoder,

    ENCODER_PATH

)

print("\n" + "=" * 60)
print("MODEL SAVED")
print("=" * 60)

print(f"\nModel   : {MODEL_PATH}")
print(f"Encoder : {ENCODER_PATH}")

print("\nTraining Completed Successfully ✅")