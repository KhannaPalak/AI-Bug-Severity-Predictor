import pickle

label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

rf = pickle.load(open("models/random_forest.pkl", "rb"))

xgb = pickle.load(open("models/xgboost.pkl", "rb"))

vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))

samples = [
    "Application crashes immediately after startup.",
    "Spelling mistake in About page.",
    "Payment gateway completely unavailable.",
    "Login button overlaps with text.",
    "Server data is permanently deleted.",
]

print("Classes:")
print(label_encoder.classes_)
print()

for text in samples:

    X = vectorizer.transform([text])

    rf_pred = label_encoder.inverse_transform(rf.predict(X))[0]

    xgb_pred = label_encoder.inverse_transform(xgb.predict(X))[0]

    print("=" * 60)
    print("Bug:", text)
    print("Random Forest :", rf_pred)
    print("XGBoost       :", xgb_pred)
