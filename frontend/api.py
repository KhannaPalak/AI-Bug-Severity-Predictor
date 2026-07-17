from predict import predict_bug
from predict_rf import predict_rf
from predict_xgb import predict_xgb


def predict_severity(text, model="BERT"):
    try:
        if model == "BERT":
            severity, confidence = predict_bug(text)

        elif model == "Random Forest":
            severity, confidence = predict_rf(text)

        elif model == "XGBoost":
            severity, confidence = predict_xgb(text)

        else:
            return {"error": "Invalid model selected."}

        return {
            "Predicted Severity": severity,
            "Confidence": confidence,
        }

    except Exception as e:
        return {"error": str(e)}


def check_backend():
    try:
        # Check if the local BERT model loads correctly
        predict_bug("Test bug report")
        return True
    except Exception:
        return False
