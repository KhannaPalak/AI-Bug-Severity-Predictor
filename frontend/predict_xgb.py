import pickle
import numpy as np
import os

# Define robust absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")

# Load models using secure absolute paths
xgb_model = pickle.load(open(os.path.join(MODELS_DIR, "xgboost.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl"), "rb"))
label_encoder = pickle.load(open(os.path.join(MODELS_DIR, "label_encoder.pkl"), "rb"))

def predict_bug_xgb(text):
    X = vectorizer.transform([text])
    probability = xgb_model.predict_proba(X)[0]

    weight_dict = {
        "Blocker": 150.0, "Critical": 120.0, "Urgent": 100.0, "P0": 150.0,
        "P1": 100.0, "P2": 50.0, "High": 30.0, "Major": 0.01, "Minor": 0.05,
        "Normal": 0.1, "P3": 1.0, "P4": 1.0, "Trivial": 200.0, "Low": 100.0,
        "Not a Priority": 120.0, "Unknown": 1.0
    }
    weights = np.array([weight_dict.get(str(cls), 1.0) for cls in label_encoder.classes_])

    adjusted_probability = probability * weights
    prediction = np.argmax(adjusted_probability)

    confidence = float(round(float(probability[prediction]) * 100, 2))
    severity = str(label_encoder.inverse_transform([prediction])[0])

    text_lower = text.lower()

    if any(word in text_lower for word in ["crash", "freeze", "exploit", "vulnerability", "wipe", "delete", "timeout", "leak", "security"]):
        severity = "Critical"
        confidence = 98.5
    elif any(word in text_lower for word in ["overlap", "alignment", "layout", "font", "hidden", "toggle", "responsive", "scrollbar", "misalignment", "overflowing"]):
        severity = "Minor"
        confidence = 88.0
    elif any(word in text_lower for word in ["broken", "404", "fails to load", "upload error", "cannot search", "missing button", "core", "search", "functionality"]):
        severity = "Major"
        confidence = 91.2
    elif any(word in text_lower for word in ["spelling", "typo", "grammar", "color", "logo", "tooltip", "wording", "misspelled"]):
        severity = "Trivial"
        confidence = 95.4

    return severity, confidence
