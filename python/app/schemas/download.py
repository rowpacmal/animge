# Standard libraries
from pydantic import BaseModel


# Prompt Request Schema
class DownloadModelRequest(BaseModel):
    repo_id: str
