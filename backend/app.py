from fastapi import FastAPI

from predict import predict_bug

app = FastAPI(
    title="AI Bug Severity Predictor API",
    description="Predicts the severity level of software bug reports using Machine Learning.",
    version="1.0.0",
)
from pydantic import BaseModel


class BugReport(BaseModel):

    text: str


@app.post("/predict")
def predict(data: BugReport):

    severity = predict_bug(data.text)

    return {"Predicted Severity": severity}


@app.get("/")
def home():
    return {"message": "AI Bug Severity Predictor API is running successfully!"}
