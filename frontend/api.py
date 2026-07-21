from predict import predict_bug


def predict_severity(text):
    try:
        severity, confidence = predict_bug(text)
        return {
            "Predicted Severity": severity,
            "Confidence": confidence,
        }
    except Exception as e:
        return {"error": str(e)}
