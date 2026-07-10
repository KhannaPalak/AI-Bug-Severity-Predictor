import pickle

# Load models
rf_model = pickle.load(open("../models/random_forest.pkl", "rb"))

vectorizer = pickle.load(open("../models/tfidf_vectorizer.pkl", "rb"))

label_encoder = pickle.load(open("../models/label_encoder.pkl", "rb"))


def predict_bug_rf(text):

    X = vectorizer.transform([text])

    prediction = rf_model.predict(X)[0]

    probability = rf_model.predict_proba(X)

    confidence = round(max(probability[0]) * 100, 2)

    severity = label_encoder.inverse_transform([prediction])[0]

    return severity, confidence
