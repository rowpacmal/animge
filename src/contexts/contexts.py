# Core
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)


class ContextProvider:
    def __init__(self):
        self.error: str | None = None
        self.is_ready: bool = False
        self.pipe: StableDiffusionPipeline | None = None


app_contexts = ContextProvider()
