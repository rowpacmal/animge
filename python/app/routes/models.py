# Third-party
from fastapi import APIRouter, Request

# Local
from app.constants import REPO_ID, REPO_TOTAL_SIZE
from app.schemas import ModelRequest


# Initialize router
models_router = APIRouter(prefix="/models", tags=["models"])


# Endpoints
@models_router.get("/")
def list_models():
    return {
        "details": "List of available models",
        "models": [
            {
                "repo_id": REPO_ID,
                "type": "text-to-image",
                "device": "cuda",
                "total_size": REPO_TOTAL_SIZE,
            }
        ],
    }


@models_router.post("/load")
def load_model(request: Request, body: ModelRequest):
    return {"details": "Model loaded successfully"}
