from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import joblib

app = FastAPI()

# Load model
model = joblib.load("model_rf.pkl")

EXPECTED_NUM_FEATURES = 30  # thay bằng số lượng feature thật của bạn

class InputData(BaseModel):
    data: List[float]  # kiểm tra kiểu phần tử là float

@app.post("/predict")
def predict(input_data: InputData):
    if len(input_data.data) != EXPECTED_NUM_FEATURES:
        raise HTTPException(
            status_code=400,
            detail=f"Expected {EXPECTED_NUM_FEATURES} features, but got {len(input_data.data)}"
        )

    X = np.array([input_data.data])
    y_pred = model.predict(X)
    return {"prediction": int(y_pred[0])}
