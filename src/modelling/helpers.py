import pickle
from typing import Any

from prefect import task

@task(name="Save pickle")
def save_pickle(path: str, obj: Any):
    with open(path, "wb") as f:
        pickle.dump(obj, f)
