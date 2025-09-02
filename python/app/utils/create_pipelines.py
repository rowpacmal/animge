# Third-party libraries
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)
from diffusers.schedulers.scheduling_euler_ancestral_discrete import (
    EulerAncestralDiscreteScheduler,
)
import torch

# Local application imports
from app.constants import CACHE_DIR, REPO_ID


def create_pipeline_text_to_image(device: torch.device):
    # Load stable diffusion pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        REPO_ID,
        cache_dir=str(CACHE_DIR),
        torch_dtype=torch.float16,
        use_safetensors=True,
        custom_pipeline="lpw_stable_diffusion_xl",
        add_watermarker=False,
    )

    # Replace scheduler with Euler A
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

    # Move model to device
    pipe.to(device)

    return pipe
