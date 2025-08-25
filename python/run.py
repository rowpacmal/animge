# Standard libraries
import io
from pathlib import Path
from uuid import uuid4

# Third-party libraries
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from PIL import PngImagePlugin
from platformdirs import user_documents_dir

# Local application imports
from app.schemas import PromptRequest
from app.model import generate_image


# Initialize FastAPI
app = FastAPI()


# API Endpoints
@app.post("/generate")
def generate(req: PromptRequest):
    # Generate image from user request
    images, used_seeds = generate_image(
        prompt=req.prompt,
        negative_prompt=req.negative_prompt,
        width=req.width,
        height=req.height,
        steps=req.steps,
        cfg_scale=req.cfg_scale,
        seed=req.seed,
        batch_size=req.batch_size,
    )

    # Save temp images locally in the user's documents folder
    documents = Path(user_documents_dir())
    save_dir = documents / "Animge" / "temp"
    save_dir.mkdir(parents=True, exist_ok=True)

    png_info = PngImagePlugin.PngInfo()
    file_paths = []

    for index, image in enumerate(images):
        uuid = str(uuid4()).replace("-", "_")
        file_path = save_dir / f"temp_{uuid}.png"
        params = (
            f"{req.prompt}\n\n"
            f"Negative prompt: {req.negative_prompt}\n"
            f"Steps: {req.steps}, Sampler: Euler a, CFG scale: {req.cfg_scale}, Seed: {used_seeds[index]}, Size: {req.width}x{req.height}"
        )
        png_info.add_text("parameters", params)
        image.save(file_path, format="PNG", pnginfo=png_info)
        file_paths.append(str(file_path))

    # Return temp image paths and used seeds
    return {"paths": file_paths, "seeds": used_seeds}
