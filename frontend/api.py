import requests

from config import API_URL


def predict_severity(text, model="BERT"):

    payload = {
        "text": text,
        "model": model,
    }

    try:

        response = requests.post(API_URL, json=payload)

        if response.status_code != 200:
            return {"error": response.text}

        return response.json()

    except Exception as e:

        return {"error": str(e)}


def check_backend():

    try:
        BACKEND_URL = "https://bug-backend-service.onrender.com"

        response = requests.get(BACKEND_URL, timeout=5)

        return response.status_code == 200

    except Exception:
        return False
