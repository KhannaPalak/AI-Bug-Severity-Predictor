import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")


label_encoder = pickle.load(open(os.path.join(MODEL_DIR, "label_encoder.pkl"), "rb"))

rf = pickle.load(open(os.path.join(MODEL_DIR, "random_forest.pkl"), "rb"))

xgb = pickle.load(open(os.path.join(MODEL_DIR, "xgboost.pkl"), "rb"))

vectorizer = pickle.load(open(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"), "rb"))

samples = [
    "Application crashes immediately after startup.",
    "Spelling mistake in About page.",
    "Payment gateway completely unavailable.",
    "Login button overlaps with text.",
    "Server data is permanently deleted.",
]

# --- THE 16-CLASS EQUALIZER ---
# We systematically scale down the giants (Major/Minor)
# and hyper-boost the rare targets (Trivial, Blocker, Critical, P0)
weight_dict = {
    # High Severity Group (Needs huge boosting)
    "Blocker": 150.0,
    "Critical": 120.0,
    "Urgent": 100.0,
    "P0": 150.0,
    "P1": 100.0,
    "P2": 50.0,
    "High": 30.0,
    # Mid-Tier Dominators (SQUASHED DOWN TO REVEAL OTHERS)
    "Major": 0.01,  # Dropped drastically so it stops hogging
    "Minor": 0.05,  # Dropped drastically so it doesn't take over Major's leftovers
    "Normal": 0.1,
    "P3": 1.0,
    "P4": 1.0,
    # Low Severity / Cosmetic Group (Needs massive boosting to beat Minor)
    "Trivial": 200.0,  # Massively boosted for cosmetic bugs like typos
    "Low": 100.0,
    "Not a Priority": 120.0,
    "Unknown": 1.0,
}

# Safely apply the weights across all 16 labels in the encoder's exact sequence
weights = np.array([weight_dict.get(str(cls), 1.0) for cls in label_encoder.classes_])

print("Classes ordered in Label Encoder:")
print(label_encoder.classes_)
print()

for text in samples:
    X = vectorizer.transform([text])

    # --- Random Forest Weighted Inference ---
    rf_prob = rf.predict_proba(X)[0]
    rf_pred_idx = np.argmax(rf_prob * weights)
    rf_pred = label_encoder.inverse_transform([rf_pred_idx])[0]

    # --- XGBoost Weighted Inference ---
    xgb_prob = xgb.predict_proba(X)[0]
    xgb_pred_idx = np.argmax(xgb_prob * weights)
    xgb_pred = label_encoder.inverse_transform([xgb_pred_idx])[0]

    print("=" * 60)
    print("Bug:", text)
    print("Random Forest :", rf_pred)
    print("XGBoost       :", xgb_pred)
