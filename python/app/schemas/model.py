# Standard
from pydantic import BaseModel


# Schema
class ModelRequest(BaseModel):
    model_id: str
