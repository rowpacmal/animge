from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)
from diffusers.schedulers.scheduling_euler_ancestral_discrete import (
    EulerAncestralDiscreteScheduler,
)
from accelerate import Accelerator
import torch

# Accelerator handles GPU/CPU device
accelerator = Accelerator()
device = accelerator.device

# Load Illustrious XL
model_id = "cagliostrolab/animagine-xl-4.0"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    use_safetensors=True,
    custom_pipeline="lpw_stable_diffusion_xl",
    add_watermarker=False,
)

# Replace scheduler with Euler A
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

# Move model to device
pipe.to(device)


def generate_image(
    prompt,
    negative_prompt=None,
    width=1024,
    height=1024,
    steps=28,
    cfg_scale=7.0,
    seed=0,
):
    # Generate image
    generator = torch.Generator(device=device).manual_seed(seed)
    output = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=width,
        height=height,
        num_inference_steps=steps,
        guidance_scale=cfg_scale,
        generator=generator,
        num_images_per_prompt=1,
    )
    image = output.images[0]  # type: ignore
    return image, seed
