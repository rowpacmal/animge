# Standard libraries
from pathlib import Path

# Third-party libraries
from huggingface_hub import repo_info


# Directories
CACHE_FOLDER = Path.cwd() / "storage" / ".cache"
CACHE_FOLDER.mkdir(parents=True, exist_ok=True)


# Hugging Face Hub
_MODEL_NAME = "animagine-xl-4.0"
REPO_ID = f"cagliostrolab/{_MODEL_NAME}"

_REPO_INFO = repo_info(repo_id=REPO_ID, files_metadata=True)
_REPO_FILES_TO_DOWNLOAD = [
    f for f in _REPO_INFO.siblings or [] if not f.rfilename.startswith(_MODEL_NAME)
]
REPO_SIZE = sum(f.size or 0 for f in _REPO_FILES_TO_DOWNLOAD)
