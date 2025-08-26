# Third-party libraries
from fastapi import APIRouter, HTTPException

# Local application imports
from app.controllers import generate_images
from app.schemas import PromptRequest
from app.utils import save_images


# Initialize router
pipelines_router = APIRouter(prefix="/pipelines", tags=["pipelines"])
text_to_image_router = APIRouter(prefix="/text-to-image")


# API Endpoint
@pipelines_router.get("/")
def list_pipelines():
    return ["text-to-image"]


@text_to_image_router.post("/")
def text_to_image(req: PromptRequest):
    # Generate image from user request
    images, used_seeds = generate_images(
        prompt=req.prompt,
        negative_prompt=req.negative_prompt,
        width=req.width,
        height=req.height,
        steps=req.steps,
        cfg_scale=req.cfg_scale,
        seed=req.seed,
        batch_size=req.batch_size,
    )

    # Save images locally in the user's documents folder
    task_id, file_paths = save_images(
        images,
        req.prompt,
        req.negative_prompt,
        req.width,
        req.height,
        req.steps,
        req.cfg_scale,
        used_seeds,
    )

    # Return task id, image paths and used seeds
    return {"id": task_id, "paths": file_paths, "seeds": used_seeds}


pipelines_router.include_router(text_to_image_router)
