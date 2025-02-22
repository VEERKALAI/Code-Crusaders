from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()  # ✅ This must be defined

# Load the trained fraud detection model
model = joblib.load("fraud_model.pkl")

@app.post("/detect_fraud/")
async def detect_fraud(transaction: dict):
    transaction_data = np.array([list(transaction.values())])
    prediction = model.predict(transaction_data)
    return {"Fraud": bool(prediction[0])}
