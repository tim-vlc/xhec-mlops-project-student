import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
import numpy as np


def train(X, y, numerical_cols, categorical_cols):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LinearRegression()

    # Start an MLflow run to log this experiment
    with mlflow.start_run():

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mse = root_mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        mlflow.log_param("numerical_columns", numerical_cols)
        mlflow.log_param("categorical_columns", categorical_cols)

        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2_score", r2)

        mlflow.sklearn.log_model(
            model, "linear_regression_model", input_example=X_test.head(1))

        # Print evaluation metrics
        print(f"Mean Squared Error (MSE): {mse}")
        print(f"R-squared (R2 Score): {r2}")

        return model
