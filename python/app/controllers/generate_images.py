# Third-party libraries
from accelerate import Accelerator
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)
import torch


# Generate images
def generate_image_text_to_image(
    pipe: StableDiffusionPipeline,
    device: torch.device,
    prompt,
    negative_prompt=None,
    width=1024,
    height=1024,
    steps=28,
    cfg_scale=5.0,
    seed=0,
    batch_size=1,
):
    generators, used_seeds = [], []

    # Generate used seeds
    for i in range(batch_size):
        current_seed = seed + i
        generator = torch.Generator(device=device).manual_seed(current_seed)
        generators.append(generator)
        used_seeds.append(current_seed)

    # Create the image outputs
    output = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=width,
        height=height,
        num_inference_steps=steps,
        guidance_scale=cfg_scale,
        num_images_per_prompt=batch_size,
        generator=generators,
    )
    images = output.images  # type: ignore

    # Return images and used seeds
    return images, used_seeds
