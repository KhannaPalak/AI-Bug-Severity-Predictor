import pickle
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

MODEL_NAME = "Ahana0316/Bug_Severity_Predictor"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

# Map 16 model classes -> 5 UI severity levels
SEVERITY_MAP = {
    "Blocker": "Blocker",
    "Critical": "Critical",
    "Urgent": "Critical",
    "P0": "Blocker",
    "P1": "Critical",
    "P2": "Major",
    "High": "Major",
    "Major": "Major",
    "Minor": "Minor",
    "Normal": "Minor",
    "P3": "Minor",
    "Low": "Minor",
    "Trivial": "Trivial",
    "P4": "Trivial",
    "Not a Priority": "Trivial",
    "Unknown": "Minor",
}


def predict_bug(text):
    encoding = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128,
    )

    with torch.no_grad():
        outputs = model(**encoding)

    probabilities = torch.softmax(outputs.logits, dim=1).cpu().numpy()[0]
    prediction_idx = probabilities.argmax()
    confidence = round(float(probabilities[prediction_idx]) * 100, 2)

    raw_label = label_encoder.inverse_transform([prediction_idx])[0]
    severity = SEVERITY_MAP.get(raw_label, "Minor")

    return severity, confidence
