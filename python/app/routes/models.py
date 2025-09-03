# Third-party
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

# Local
from app.constants import REPO_ID, REPO_TOTAL_SIZE
from app.controllers import get_stable_diffusion_pipeline


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
async def load_model(request: Request):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is not None:
            raise HTTPException(
                status_code=400, detail="A model is already loaded. Unload it first."
            )

        try:
            request.app.state.pipeline = get_stable_diffusion_pipeline()

            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "error": None,
                    "message": {
                        "is_loaded": True,
                        "repo_id": REPO_ID,
                    },
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
                    "message": {
                        "is_loaded": False,
                        "repo_id": REPO_ID,
                    },
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to unload model: {str(e)}"
            )
