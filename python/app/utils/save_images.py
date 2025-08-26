# Standard libraries
from uuid import uuid4

# Third-party libraries
from PIL import PngImagePlugin

# Local application imports
from app.constants import TEMP_DIR


def save_images(
    images,
    prompt: str,
    negative_prompt: str | None,
    width: int,
    height: int,
    steps: int,
    cfg_scale: float,
    used_seeds: list[int],
):
    task_id = str(uuid4()).replace("-", "_")
    task_dir = TEMP_DIR / task_id
    task_dir.mkdir(parents=True, exist_ok=True)

    png_info = PngImagePlugin.PngInfo()
    file_paths = []

    for index, image in enumerate(images):
        file_path = task_dir / f"{index:02}.png"
        params = (
            f"{prompt}\n\n"
            f"Negative prompt: {negative_prompt}\n"
            f"Steps: {steps}, Sampler: Euler a, CFG scale: {cfg_scale}, Seed: {used_seeds[index]}, Size: {width}x{height}"
        )
        png_info.add_text("parameters", params)
        image.save(file_path, format="PNG", pnginfo=png_info)
        file_paths.append(str(file_path))

    return task_id, file_paths
