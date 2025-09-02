from diffusers.schedulers.scheduling_euler_ancestral_discrete import (
    EulerAncestralDiscreteScheduler,
)
from diffusers.schedulers.scheduling_euler_discrete import EulerDiscreteScheduler
from diffusers.schedulers.scheduling_ddim import DDIMScheduler
from diffusers.utils.dummy_pt_objects import DPMSolverMultistepScheduler


def get_scheduler(scheduler_type: str, config: dict):
    # Euler
    if scheduler_type == "euler":
        return EulerDiscreteScheduler.from_config(config)
    elif scheduler_type == "euler_a":
        return EulerAncestralDiscreteScheduler.from_config(config)

    # DPM
    elif scheduler_type == "dpmpp_2m":
        return DPMSolverMultistepScheduler.from_config(config)
    elif scheduler_type == "dpmpp_2m_karras":
        return DPMSolverMultistepScheduler.from_config(config, use_karras_sigmas=True)

    # DDIM
    elif scheduler_type == "ddim":
        return DDIMScheduler.from_config(config)

    # Everything Else
    else:
        raise ValueError(f"Unknown scheduler type: {scheduler_type}")
