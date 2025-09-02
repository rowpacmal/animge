# Third-party
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import torch

# Local
from app.constants import REPO_ID, REPO_TOTAL_SIZE
from app.controllers.models import get_pipeline_by_repo_id
from app.schemas import (
    LoadModelRequest,
    UpdateModelDeviceRequest,
    UpdateModelSchedulerRequest,
)
from app.utils import get_scheduler


# Initialize router
models_router = APIRouter(prefix="/models", tags=["models"])


# Endpoints
@models_router.get("/")
def list_models():
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "error": None,
            "message": [
                {
                    "repo_id": REPO_ID,
                    "type": "text-to-image",
                    "device": "cuda",
                    "total_size": REPO_TOTAL_SIZE,
                }
            ],
        },
    )


@models_router.post("/load")
async def load_model(request: Request, body: LoadModelRequest):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is not None:
            raise HTTPException(
                status_code=400, detail="A model is already loaded. Unload it first."
            )

        try:
            request.app.state.pipeline = get_pipeline_by_repo_id(
                body.repo_id, body.scheduler_type, torch.device(body.device)
            )

            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "error": None,
                    "message": f"Model '{body.repo_id}' loaded.",
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to load model: {str(e)}"
            )


@models_router.post("/unload")
async def unload_model(request: Request):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is None:
            raise HTTPException(status_code=400, detail="No model is loaded.")

        try:
            request.app.state.pipeline = None

            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "error": None,
                    "message": "Model unloaded.",
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to unload model: {str(e)}"
            )


@models_router.patch("/scheduler")
async def update_scheduler(request: Request, body: UpdateModelSchedulerRequest):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is None:
            raise HTTPException(status_code=400, detail="No model is loaded.")

        try:
            request.app.state.pipeline.scheduler = get_scheduler(
                body.scheduler_type, request.app.state.pipeline.scheduler.config
            )

            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "error": None,
                    "message": f"Scheduler updated to '{body.scheduler_type}'.",
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to update scheduler: {str(e)}"
            )


@models_router.patch("/device")
async def update_device(request: Request, body: UpdateModelDeviceRequest):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is None:
            raise HTTPException(status_code=400, detail="No model is loaded.")

        try:
            request.app.state.pipeline.to(torch.device(body.device))

            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "error": None,
                    "message": f"Device updated to '{body.device}'.",
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to update device: {str(e)}"
            )
