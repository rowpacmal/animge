# Third-party
import torch
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)


def get_generated_images(
    pipeline: StableDiffusionPipeline,
    prompt: str,
    negative_prompt: str | None,
    width: int,
    height: int,
    steps: int,
    cfg_scale: float,
    seed: int,
    batch_size: int,
):
    generators, used_seeds = [], []

    for i in range(batch_size):
        current_seed = seed + i
        generator = torch.Generator(device=torch.device("cuda")).manual_seed(
            current_seed
        )
        generators.append(generator)
        used_seeds.append(current_seed)

    output = pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=width,
        height=height,
        num_inference_steps=steps,
        guidance_scale=cfg_scale,
        num_images_per_prompt=batch_size,
        generator=generators,
    )
    images, _ = output

    return images, used_seeds
