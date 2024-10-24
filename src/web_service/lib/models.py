# Pydantic models for the web service
from typing import Literal
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
    Sex: Literal["M"] | Literal["F"] | Literal["I"]

# Define response model
class PredictionResponse(BaseModel):
    Rings: int