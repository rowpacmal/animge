# Third-party
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)
import torch


# Local
from app.constants import CACHE_DIR
from app.utils import get_scheduler


def get_pipeline_by_repo_id(repo_id: str, scheduler_type: str, device: torch.device):
    pipe = StableDiffusionPipeline.from_pretrained(
        repo_id,
        cache_dir=str(CACHE_DIR),
        torch_dtype=torch.float16,
        use_safetensors=True,
        custom_pipeline="lpw_stable_diffusion_xl",
        add_watermarker=False,
    )

    pipe.scheduler = get_scheduler(scheduler_type, pipe.scheduler.config)
    pipe.to(device)

    return pipe
