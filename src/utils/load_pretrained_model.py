# Core
from accelerate import Accelerator
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)
from diffusers.schedulers.scheduling_euler_ancestral_discrete import (
    EulerAncestralDiscreteScheduler,
)
import torch

# Application
from constants import CACHE_FOLDER, REPO_ID


def load_pretrained_model():
    accelerator = Accelerator()
    device = accelerator.device

    pipe = StableDiffusionPipeline.from_pretrained(
        REPO_ID,
        cache_dir=str(CACHE_FOLDER),
        torch_dtype=torch.float16,
        use_safetensors=True,
        custom_pipeline="lpw_stable_diffusion_xl",
        add_watermarker=False,
    )

    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe.to(device)

    return pipe
