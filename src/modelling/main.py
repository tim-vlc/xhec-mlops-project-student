# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.
import os

from prefect import serve
from src.modelling.config import DATA_DIRPATH, MODELS_DIRPATH
from src.modelling.workflows import train_model_workflow

if __name__ == "__main__":
    train_model_deployment = train_model_workflow.to_deployment(
        name="Model Training Deployment",
        version="0.1.0",
        tags=["training", "model"],
        cron="0 0 * * 0",
        parameters={
            "filepath": os.path.join(DATA_DIRPATH, "abalone.csv"),
            "artifacts_filepath": MODELS_DIRPATH,
        },
    )

    serve(train_model_deployment)
