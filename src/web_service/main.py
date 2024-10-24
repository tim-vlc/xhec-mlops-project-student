# Code with FastAPI (app = FastAPI(...))


import os
import pandas as pd
from fastapi import FastAPI
from lib.models import PredictionResponse
from lib.models import InputData
from utils import load_object
from lib.inference import run_inference
from app_config import MODELS_DIRPATH

# Other imports

app = FastAPI(title="...", description="...")


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionResponse, status_code=201)
def predict(payload: InputData) -> dict:
    model = load_object(os.path.join(MODELS_DIRPATH, "model.pkl"))
    y = run_inference([payload], model)

    return {"number_rings_prediction": y[0]}
