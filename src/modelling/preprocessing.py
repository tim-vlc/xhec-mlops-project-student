from sklearn.preprocessing import OneHotEncoder
from prefect import task
import pandas as pd


@task
def preprocess_data(df, numerical_cols, categorical_cols, target_col):
    encoder = OneHotEncoder(drop="first", sparse_output=False)
    encoded_categorical = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(
        encoded_categorical, columns=encoder.get_feature_names_out(categorical_cols)
    )

    X = pd.concat([df[numerical_cols], encoded_df], axis=1)
    y = df[target_col]

    return X, y, encoder
