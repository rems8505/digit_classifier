from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_digit

app = FastAPI()

# Input data format
class DigitInput(BaseModel):
    features: list

# Prediction endpoint
@app.post("/predict")
def predict(input: DigitInput):
    pred = predict_digit(input.features)
    return {"prediction": pred}
es: list

@app.post("/predict")
def predict(input: DigitInput):
    pred = predict_digit(input.features)
    return {"prediction": pred}
