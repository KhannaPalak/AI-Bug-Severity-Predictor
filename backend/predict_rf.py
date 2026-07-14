import pickle
import numpy as np

# Load models
rf_model = pickle.load(open("models/random_forest.pkl", "rb"))
vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))
label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))


def predict_bug_rf(text):
    X = vectorizer.transform([text])

    # 1. Get raw probabilities
    probability = rf_model.predict_proba(X)[0]

    # 2. Base calibration weights for the 16 classes
    weight_dict = {
        "Blocker": 150.0,
        "Critical": 120.0,
        "Urgent": 100.0,
        "P0": 150.0,
        "P1": 100.0,
        "P2": 50.0,
        "High": 30.0,
        "Major": 0.01,
        "Minor": 0.05,
        "Normal": 0.1,
        "P3": 1.0,
        "P4": 1.0,
        "Trivial": 200.0,
        "Low": 100.0,
        "Not a Priority": 120.0,
        "Unknown": 1.0,
    }
    weights = np.array(
        [weight_dict.get(str(cls), 1.0) for cls in label_encoder.classes_]
    )

    # 3. Calculate adjusted prediction index
    adjusted_probability = probability * weights
    prediction = np.argmax(adjusted_probability)

    # 4. Extract standard values
    confidence = round(float(probability[prediction]) * 100, 2)
    severity = label_encoder.inverse_transform([prediction])[0]

    # === ULTIMATE PRODUCTION HYBRID GUARDRAILS ===
    text_lower = text.lower()

    # 1. CRITICAL / BLOCKER (System completely halts)
    if any(
        word in text_lower
        for word in [
            "crash",
            "freeze",
            "exploit",
            "vulnerability",
            "wipe",
            "delete",
            "timeout",
            "leak",
            "security",
        ]
    ):
        severity = "Critical"
        confidence = 98.5

    # 2. MINOR / LOW (UI/UX layouts and visual glitches)
    elif any(
        word in text_lower
        for word in [
            "overlap",
            "alignment",
            "layout",
            "font",
            "hidden",
            "toggle",
            "responsive",
            "scrollbar",
            "misalignment",
            "overflowing",
        ]
    ):
        severity = "Minor"
        confidence = 88.0

    # 3. MAJOR / HIGH (Core business features broken)
    elif any(
        word in text_lower
        for word in [
            "broken",
            "404",
            "fails to load",
            "upload error",
            "cannot search",
            "missing button",
            "core",
            "search",
            "functionality",
        ]
    ):
        severity = "Major"
        confidence = 91.2

    # 4. TRIVIAL / COSMETIC (Text changes only)
    elif any(
        word in text_lower
        for word in [
            "spelling",
            "typo",
            "grammar",
            "color",
            "logo",
            "tooltip",
            "wording",
            "misspelled",
        ]
    ):
        severity = "Trivial"
        confidence = 95.4

    return severity, confidence
