# Third-party libraries
from fastapi import APIRouter, HTTPException

# Local application imports
from .pipelines import txt2img_router

# Initialize router
models_router = APIRouter(prefix="/models", tags=["models"])
versions_router = APIRouter(prefix="/{model_name}/versions")


# API Endpoints
@models_router.get("/")
async def list_models():
    models = ["animagine-xl"]

    return models


@versions_router.get("/")
async def list_versions(model_name: str):
    versions = {
        "animagine-xl": ["v4"],
    }

    if model_name not in versions:
        raise HTTPException(status_code=404, detail="Model not found")

    return versions[model_name]


# Include routers
versions_router.include_router(txt2img_router)
models_router.include_router(versions_router)
