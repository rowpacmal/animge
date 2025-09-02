# Standard
from pydantic import BaseModel


# Schemas
class LoadModelRequest(BaseModel):
    repo_id: str
    scheduler_type: str = "euler_a"
    device: str = "cuda"


class UpdateModelDeviceRequest(BaseModel):
    device: str = "cuda"


class UpdateModelSchedulerRequest(BaseModel):
    scheduler_type: str = "euler_a"
