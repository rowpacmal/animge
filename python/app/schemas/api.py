# Standard
from typing import Any
from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    error: str | None = None
    message: str
    data: Any | None = None
