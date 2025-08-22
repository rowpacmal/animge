# Standard libraries
import io
from pathlib import Path

# Third-party libraries
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
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
    image, used_seed = generate_image(
        prompt=req.prompt,
        negative_prompt=req.negative_prompt,
        width=req.width,
        height=req.height,
        steps=req.steps,
        cfg_scale=req.cfg_scale,
        seed=req.seed,
    )

    # Save temp image locally in the user's documents folder
    documents = Path(user_documents_dir())
    save_dir = documents / "Animge" / "temp"
    save_dir.mkdir(parents=True, exist_ok=True)

    file_path = save_dir / f"temp_{used_seed}.png"
    image.save(file_path, format="PNG")

    # Return temp image path and used seed
    return {"path": str(file_path), "seed": used_seed}
