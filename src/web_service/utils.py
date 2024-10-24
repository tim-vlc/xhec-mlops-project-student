# Utils file. TODO: add a `load_object` function to load pickle objects
import pickle

def load_object(path: str):
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj