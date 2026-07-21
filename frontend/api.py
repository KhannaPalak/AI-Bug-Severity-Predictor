import os
import requests

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:8000")


def predict_severity(text):
    try:
        resp = requests.post(
            f"{BACKEND_URL}/predict",
            json={"text": text},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.ConnectionError:
        return {"error": f"Cannot connect to backend at {BACKEND_URL}. Is it running?"}
    except Exception as e:
        return {"error": str(e)}
