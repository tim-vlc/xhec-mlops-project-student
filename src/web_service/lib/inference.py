

from typing import List
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.preprocessing import OneHotEncoder
from app_config import CATEGORICAL_COLS, NUMERICAL_COLS, TARGET_COLS
from loguru import logger
import numpy as np

from models import InputData

def preprocess_X(df: pd.DataFrame):
    encoder = OneHotEncoder(drop="first", sparse_output=False)
    encoded_categorical = encoder.fit_transform(df[CATEGORICAL_COLS])
    encoded_df = pd.DataFrame(
        encoded_categorical, columns=encoder.get_feature_names_out(CATEGORICAL_COLS)
    )

    X = pd.concat([df[NUMERICAL_COLS], encoded_df], axis=1)

    return X

def run_inference(input_data: List[InputData], model: BaseEstimator) -> np.ndarray:
    """Run inference on a list of input data.
    Args:
        payload (dict): the data point to run inference on.
        model (BaseEstimator): the fitted model object.
    Returns:
        np.ndarray: the predicted trip durations in minutes.
    Example payload:
        {'PULocationID': 264, 'DOLocationID': 264, 'passenger_count': 1}
    """
    logger.info(f"Running inference on:\n{input_data}")
    df = pd.DataFrame([x.dict() for x in input_data])
    X = preprocess_X(df)

    y = model.predict(X)
    logger.info(f"Predicted trip durations:\n{y}")
    return y