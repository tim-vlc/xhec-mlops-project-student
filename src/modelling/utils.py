# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).
import pickle
import os


def pickle_object(model):

    model_directory = 'src/web_service/local_objects'
    # Create the directory if it doesn't exist
    os.makedirs(model_directory, exist_ok=True)
    model_path = os.path.join(model_directory, 'model.pkl')

    # Save the model to a .pkl file
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
