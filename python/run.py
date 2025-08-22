from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io
from app.schemas import PromptRequest
from app.model import generate_image


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

    # Save image to in-memory bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # You could also include used_seed in headers or JSON response if needed
    return StreamingResponse(img_bytes, media_type="image/png")
