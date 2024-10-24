import os
from fastapi import FastAPI
import uvicorn
from lib.models import PredictionResponse
from lib.models import InputData
from utils import load_object
from lib.inference import run_inference
from app_config import MODELS_DIRPATH

from app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION
)
from fastapi import FastAPI

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionResponse, status_code=201)
def predict(payload: InputData) -> dict:
    model = load_object(os.path.join(MODELS_DIRPATH, "model.pkl"))
    encoder = load_object(os.path.join(MODELS_DIRPATH, "encoder.pkl"))
    y = run_inference([payload], model, encoder)

    return {"Rings": int(y[0])}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)