from predict import predict_bug
from predict_rf import predict_bug_rf
from predict_xgb import predict_bug_xgb

def predict_severity(text, model="BERT"):
    try:
        if model == "BERT":
            severity, confidence = predict_bug(text)

        elif model == "Random Forest":
            severity, confidence = predict_bug_rf(text)

        elif model == "XGBoost":
            severity, confidence = predict_bug_xgb(text)

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
        predict_bug("Test bug report")
        return True
    except Exception:
        return False
