from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- ADD THIS IMPORT

from predict import predict_bug
from predict_rf import predict_bug_rf
from predict_xgb import predict_bug_xgb

app = FastAPI(
    title="AI Bug Severity Predictor API",
    description="Predicts the severity level of software bug reports using Machine Learning.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (local and deployed)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------------------------


class BugReport(BaseModel):
    text: str
    model: str = "BERT"


from pydantic import BaseModel


class BugReport(BaseModel):

    text: str

    model: str = "BERT"


@app.post("/predict")
def predict(data: BugReport):

    try:

        if data.model == "BERT":

            severity, confidence = predict_bug(data.text)

        elif data.model == "Random Forest":

            severity, confidence = predict_bug_rf(data.text)

        elif data.model == "XGBoost":

            severity, confidence = predict_bug_xgb(data.text)

        else:

            severity, confidence = predict_bug(data.text)

        return {
            "Predicted Severity": severity,
            "Confidence": confidence,
        }

    except Exception as e:

        print(e)
        return {"error": str(e)}


@app.get("/")
def home():
    return {"message": "AI Bug Severity Predictor API is running successfully!"}


@app.get("/health")
def health():
    return {"status": "healthy", "message": "Backend is running"}
