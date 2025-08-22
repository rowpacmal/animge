from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io
from app.schemas import PromptRequest
from app.model import generate_image
from pathlib import Path
from platformdirs import user_documents_dir


app = FastAPI()


@app.post("/generate")
def generate(req: PromptRequest):
    image, used_seed = generate_image(
        prompt=req.prompt,
        negative_prompt=req.negative_prompt,
        width=req.width,
        height=req.height,
        steps=req.steps,
        cfg_scale=req.cfg_scale,
        seed=req.seed,
    )

    documents = Path(user_documents_dir())
    save_dir = documents / "MyApp"
    save_dir.mkdir(parents=True, exist_ok=True)

    file_path = save_dir / f"generated_{used_seed}.png"
    image.save(file_path, format="PNG")

    return {"path": str(file_path), "seed": used_seed}
