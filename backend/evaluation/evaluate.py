import json
import requests
from pathlib import Path


# =========================================
# CONFIGURATION
# =========================================

API_URL = "http://127.0.0.1:8000/detect-conflict"

GROUND_TRUTH_FILE = Path(__file__).parent / "ground_truth.json"

RESULTS_FILE = Path(__file__).parent / "results.json"

# =========================================
# LOAD GROUND TRUTH
# =========================================

with open(
    GROUND_TRUTH_FILE,
    "r",
    encoding="utf-8"
) as f:

    ground_truth = json.load(f)

cases = ground_truth["clauses"]



# =========================================
# METRICS
# =========================================

TP = 0
FP = 0
TN = 0
FN = 0

results = []

# =========================================
# EVALUATE EACH TEST CASE
# =========================================

for case in cases:

    print(f"Evaluating {case['id']}...")

    # -------------------------------------
    # Build API Request
    # -------------------------------------

    payload = {
        "query": case["internal_clause"]
    }

    # -------------------------------------
    # Call FastAPI
    # -------------------------------------

    response = requests.post(
        API_URL,
        json=payload
    )

    # Check request success

    if response.status_code != 200:

        print(f"❌ Failed on {case['id']}")

        continue

    prediction = response.json()

    # -------------------------------------
    # Expected Label
    # -------------------------------------

    expected_conflict = (
        case["label"] == "CONFLICT"
    )

    # -------------------------------------
    # Model Prediction
    # -------------------------------------

    predicted_conflict = prediction.get(
        "conflict_detected",
        False
    )

    # -------------------------------------
    # Update Confusion Matrix
    # -------------------------------------

    if expected_conflict and predicted_conflict:

        TP += 1

        result = "TP"

    elif expected_conflict and not predicted_conflict:

        FN += 1

        result = "FN"

    elif not expected_conflict and predicted_conflict:

        FP += 1

        result = "FP"

    else:

        TN += 1

        result = "TN"

    # -------------------------------------
    # Save Result
    # -------------------------------------

    results.append({

        "id": case["id"],

        "expected": case["label"],

        "predicted": (
            "CONFLICT"
            if predicted_conflict
            else "NO_CONFLICT"
        ),

        "result": result,

        "risk_level": prediction.get("risk_level"),

        "reason": prediction.get("reason")
    })

    # =========================================
# CALCULATE METRICS
# =========================================

total = TP + FP + TN + FN

accuracy = (TP + TN) / total if total else 0

precision = TP / (TP + FP) if (TP + FP) else 0

recall = TP / (TP + FN) if (TP + FN) else 0

f1_score = (
    2 * precision * recall / (precision + recall)
    if (precision + recall)
    else 0
)

# =========================================
# PRINT REPORT
# =========================================

print("\n")
print("=" * 50)
print("RegMind AI Evaluation Report")
print("=" * 50)

print(f"Total Test Cases : {total}")

print(f"True Positives   : {TP}")
print(f"False Positives  : {FP}")
print(f"True Negatives   : {TN}")
print(f"False Negatives  : {FN}")

print("-" * 50)

print(f"Accuracy         : {accuracy:.2%}")
print(f"Precision        : {precision:.2%}")
print(f"Recall           : {recall:.2%}")
print(f"F1 Score         : {f1_score:.2%}")

print("=" * 50)



# =========================================
# SAVE RESULTS
# =========================================

summary = {
    "metrics": {
        "total_cases": total,
        "true_positives": TP,
        "false_positives": FP,
        "true_negatives": TN,
        "false_negatives": FN,
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1_score, 4)
    },
    "predictions": results
}

with open(
    RESULTS_FILE,
    "w",
    encoding="utf-8"
) as f:
    json.dump(summary, f, indent=4)

print("\n✅ Results saved to:")
print(RESULTS_FILE)