# Pydantic models for the web service
from pydantic import BaseModel


# Define request model
class InputData(BaseModel):
    Length: float
    Diameter: float
    Height: float
    Whole_weight: float
    Shucked_weight: float
    Viscera_weight: float
    Shell_weight: float
    Sex: str


# Define response model
class PredictionResponse(BaseModel):
    Rings: int
