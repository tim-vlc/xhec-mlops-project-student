import os
from typing import Optional

import pandas as pd
from sklearn.model_selection import train_test_split
from helpers import save_pickle
from loguru import logger


from prefect import flow
from preprocessing import preprocess_data
from config import NUMERICAL_COLS, CATEGORICAL_COLS, TARGET_COLS
from modeling import train_model, predict, evaluate_model


@flow(name="Train model")
def train_model_workflow(
    filepath: str,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    """Train a model and save it to a file"""

    logger.info("Loading data...")
    df = pd.read_csv(filepath)

    logger.info("Processing data...")
    X, y = preprocess_data(df, NUMERICAL_COLS, CATEGORICAL_COLS, TARGET_COLS)

    logger.info("Splitting train and test data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    logger.info("Training model...")
    model = train_model(X_train, y_train)

    logger.info("Making predictions and evaluating...")
    y_pred = predict(X_test, model)
    rmse = evaluate_model(y_test, y_pred)

    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        save_pickle(os.path.join(artifacts_filepath, "model.pkl"), model)

    return {"model": model, "rmse": rmse}


if __name__ == "__main__":
    from config import DATA_DIRPATH, MODELS_DIRPATH

    train_model_workflow(
        filepath=os.path.join(DATA_DIRPATH, "abalone.csv"),
        artifacts_filepath=MODELS_DIRPATH,
    )
