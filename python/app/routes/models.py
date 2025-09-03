# Third-party
from fastapi import APIRouter, HTTPException, Request
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

# Local
from app.constants import REPO_ID, REPO_TOTAL_SIZE
from app.controllers import get_stable_diffusion_pipeline
from app.schemas import ApiResponse


# Initialize router
models_router = APIRouter(prefix="/models", tags=["models"])


# Endpoints
@models_router.get("/", response_model=ApiResponse, status_code=HTTP_200_OK)
def list_models():
    return ApiResponse(
        success=True,
        error=None,
        message="Models list retrieved successfully.",
        data=[
            {
                "repo_id": REPO_ID,
                "type": "text-to-image",
                "device": "cuda",
                "total_size": REPO_TOTAL_SIZE,
            }
        ],
    )


@models_router.post("/load", response_model=ApiResponse, status_code=HTTP_200_OK)
async def load_model(request: Request):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is not None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="A model is already loaded. Unload it first.",
            )

        try:
            request.app.state.pipeline = get_stable_diffusion_pipeline()

            return ApiResponse(
                success=True,
                error=None,
                message="Model loaded successfully.",
                data={
                    "is_loaded": True,
                    "repo_id": REPO_ID,
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to load model: {str(e)}",
            )


@models_router.post("/unload", response_model=ApiResponse, status_code=HTTP_200_OK)
async def unload_model(request: Request):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="No model is loaded."
            )

        try:
            request.app.state.pipeline = None

            return ApiResponse(
                success=True,
                error=None,
                message="Model unloaded successfully.",
                data={
                    "is_loaded": False,
                    "repo_id": REPO_ID,
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to unload model: {str(e)}",
            )
