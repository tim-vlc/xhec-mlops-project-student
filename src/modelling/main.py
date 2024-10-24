# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
from pathlib import Path
import pandas as pd
from preprocessing import preprocess_data
from training import train
from utils import pickle_object


def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    df = pd.read_csv(trainset_path)
    numerical_cols = ['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
                      'Viscera weight', 'Shell weight']
    categorical_cols = ['Sex']
    target_col = ['Rings']
    # Preprocess data
    X, y = preprocess_data(df, numerical_cols, categorical_cols, target_col)
    # (Optional) Pickle encoder if need be

    # Train model
    model = train(X, y, numerical_cols, categorical_cols)
    # Pickle model --> The model should be saved in pkl format the `src/web_service/local_objects` folder
    pickle_object(model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str,
                        help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
