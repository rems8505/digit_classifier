import joblib
import numpy as np

# Load pre-trained model
model = joblib.load("digit_model/digits_model.pkl")

# Prediction function
def predict_digit(features):
    prediction = model.predict([features])
    return int(prediction[0])
