

from typing import List
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.preprocessing import OneHotEncoder
from app_config import CATEGORICAL_COLS, NUMERICAL_COLS
from loguru import logger
import numpy as np

from lib.models import InputData

def preprocess_X(df: pd.DataFrame, encoder: OneHotEncoder):
    encoded_categorical = encoder.transform(df[CATEGORICAL_COLS].astype('category'))
    encoded_df = pd.DataFrame(
        encoded_categorical, columns=encoder.get_feature_names_out(CATEGORICAL_COLS)
    )

    X = pd.concat([df[NUMERICAL_COLS], encoded_df], axis=1)

    return X

def run_inference(input_data: List[InputData], model: BaseEstimator, encoder: OneHotEncoder) -> np.ndarray:
    logger.info(f"Running inference on:\n{input_data}")

    print(input_data[0].model_dump())

    df = pd.DataFrame([
        {key.replace("_", " "):value for key, value in x.model_dump().items()}
        for x in input_data
    ],
    columns = NUMERICAL_COLS + CATEGORICAL_COLS)

    X = preprocess_X(df, encoder)

    y = model.predict(X)
    logger.info(f"Predicted trip durations:\n{y}")
    return y