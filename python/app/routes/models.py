# Third-party libraries
from fastapi import APIRouter, HTTPException

# Local application imports
from .pipelines import txt2img_router
from app.constants import MODEL_TYPES, MODEL_VERSIONS

# Initialize router
models_router = APIRouter(prefix="/models", tags=["models"])
versions_router = APIRouter(prefix="/{model_name}/versions")


# API Endpoints
@models_router.get("/")
def list_models():
    return MODEL_TYPES


@versions_router.get("/")
def list_versions(model_name: str):
    if model_name not in MODEL_VERSIONS:
        raise HTTPException(status_code=404, detail="Model not found")

    return MODEL_VERSIONS[model_name]


# Include routers
versions_router.include_router(txt2img_router)
models_router.include_router(versions_router)
