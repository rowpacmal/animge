# Third-party
from diffusers.pipelines.stable_diffusion_xl.pipeline_stable_diffusion_xl import (
    StableDiffusionXLPipeline,
)
from diffusers.schedulers.scheduling_euler_ancestral_discrete import (
    EulerAncestralDiscreteScheduler,
)
import torch


# Local
from app.constants import CACHE_DIR, REPO_ID


def get_stable_diffusion_pipeline():
    pipe = StableDiffusionXLPipeline.from_pretrained(
        REPO_ID,
        cache_dir=str(CACHE_DIR),
        torch_dtype=torch.float16,
        use_safetensors=True,
        custom_pipeline="lpw_stable_diffusion_xl",
        add_watermarker=False,
    )

    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe.to(torch.device("cuda"))

    return pipe
