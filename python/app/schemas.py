# Standard libraries
from pydantic import BaseModel


# Prompt Request Schema
class PromptRequest(BaseModel):
    prompt: str
    negative_prompt: str | None = None
    width: int = 1024
    height: int = 1024
    steps: int = 28
    cfg_scale: float = 7.0
    seed: int = 0
    batch_size: int = 1
