# Standard
from pydantic import BaseModel


# Schema
class PromptRequest(BaseModel):
    prompt: str
    negative_prompt: str | None = None
    width: int = 1024
    height: int = 1024
    steps: int = 28
    cfg_scale: float = 5.0
    seed: int = 0
    batch_size: int = 1
