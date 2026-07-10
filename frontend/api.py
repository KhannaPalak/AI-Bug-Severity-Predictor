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

        response = requests.get("http://127.0.0.1:8000/")

        return response.status_code == 200

    except:

        return False
