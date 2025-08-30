# Standard libraries
from pathlib import Path

# Third-party libraries
from huggingface_hub import model_info


# Directories
CACHE_FOLDER = Path.cwd() / "storage" / ".cache"
CACHE_FOLDER.mkdir(parents=True, exist_ok=True)


# Hugging Face Hub
REPO_ID = "cagliostrolab/animagine-xl-4.0"

_MODEL_INFO = model_info(repo_id=REPO_ID, files_metadata=True)
_MODEL_SIBLINGS = _MODEL_INFO.siblings or []
MODEL_SIZE = sum(f.size or 0 for f in _MODEL_SIBLINGS)
