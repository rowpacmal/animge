# Third-party
from fastapi import APIRouter, HTTPException, Request
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

# Local
from app.controllers import get_generated_images
from app.schemas import ApiResponse, PromptRequest
from app.utils import save_images


# Initialize router
images_router = APIRouter(prefix="/images", tags=["images"])


# Endpoints
@images_router.post("/", response_model=ApiResponse, status_code=HTTP_200_OK)
async def generate_images(request: Request, body: PromptRequest):
    async with request.app.state.api_lock:
        if request.app.state.pipeline is None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="No model is loaded.",
            )

        try:
            images, used_seeds = get_generated_images(
                pipeline=request.app.state.pipeline,
                prompt=body.prompt,
                negative_prompt=body.negative_prompt,
                width=body.width,
                height=body.height,
                steps=body.steps,
                cfg_scale=body.cfg_scale,
                seed=body.seed,
                batch_size=body.batch_size,
            )

            task_id, file_paths = save_images(
                images=images,
                prompt=body.prompt,
                negative_prompt=body.negative_prompt,
                width=body.width,
                height=body.height,
                steps=body.steps,
                cfg_scale=body.cfg_scale,
                used_seeds=used_seeds,
            )

            return ApiResponse(
                message="Images generated successfully.",
                data={
                    "task_id": task_id,
                    "file_paths": file_paths,
                    "used_seeds": used_seeds,
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to generate images: {str(e)}",
            )
