# Third-party libraries
from accelerate import Accelerator
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)
from diffusers.schedulers.scheduling_euler_ancestral_discrete import (
    EulerAncestralDiscreteScheduler,
)
import torch

from pathlib import Path
from platformdirs import user_documents_dir

# Accelerator handles GPU/CPU device
accelerator = Accelerator()
device = accelerator.device

# Load AnimagineXL v4.0 model
model_id = "cagliostrolab/animagine-xl-4.0"
documents = Path(user_documents_dir())
cache_dir = documents / "Animge" / "models"
cache_dir.mkdir(parents=True, exist_ok=True)
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    cache_dir=str(cache_dir),
    torch_dtype=torch.float16,
    use_safetensors=True,
    custom_pipeline="lpw_stable_diffusion_xl",
    add_watermarker=False,
)

# Replace scheduler with Euler A
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

# Move model to device
pipe.to(device)


# Generate images
def generate_images(
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

    # Generate random seeds
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
