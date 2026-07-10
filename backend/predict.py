import pickle
import torch

from transformers import BertTokenizer
from transformers import BertForSequenceClassification

# ----------------------------
# Load Label Encoder
# ----------------------------

label_encoder = pickle.load(open("../models/label_encoder.pkl", "rb"))

# ----------------------------
# Load Tokenizer
# ----------------------------

tokenizer = BertTokenizer.from_pretrained("../models/bert_model")

# ----------------------------
# Load Trained BERT
# ----------------------------

model = BertForSequenceClassification.from_pretrained("../models/bert_model")

model.eval()

# ----------------------------
# Prediction Function
# ----------------------------


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

    probabilities = torch.softmax(outputs.logits, dim=1)

    confidence = round(
        probabilities.max().item() * 100,
        2,
    )

    prediction = torch.argmax(outputs.logits, dim=1).item()

    severity = label_encoder.inverse_transform([prediction])[0]

    return severity, confidence
