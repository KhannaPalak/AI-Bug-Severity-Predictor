from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from predict import predict_bug

app = FastAPI(
    title="AI Bug Severity Predictor API",
    description="Predicts the severity level of software bug reports using BERT.",
    version="1.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BugReport(BaseModel):
    text: str


@app.post("/predict")
def predict(data: BugReport):
    try:
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
