import pickle

rf_model = pickle.load(open("../models/random_forest.pkl","rb"))

xgb_model = pickle.load(open("../models/xgboost.pkl","rb"))

tfidf = pickle.load(open("../models/tfidf_vectorizer.pkl","rb"))

label_encoder = pickle.load(open("../models/label_encoder.pkl","rb"))

def predict_bug(text):

    vector = tfidf.transform([text])

    prediction = xgb_model.predict(vector)

    severity = label_encoder.inverse_transform(prediction)

    return severity[0]