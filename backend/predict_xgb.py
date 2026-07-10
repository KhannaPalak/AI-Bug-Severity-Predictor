import pickle

# Load models
xgb_model = pickle.load(open("../models/xgboost.pkl", "rb"))

vectorizer = pickle.load(open("../models/tfidf_vectorizer.pkl", "rb"))

label_encoder = pickle.load(open("../models/label_encoder.pkl", "rb"))


def predict_bug_xgb(text):

    X = vectorizer.transform([text])

    prediction = int(xgb_model.predict(X)[0])

    probability = xgb_model.predict_proba(X)

    confidence = float(round(float(max(probability[0])) * 100, 2))

    severity = str(label_encoder.inverse_transform([prediction])[0])

    return severity, confidence
