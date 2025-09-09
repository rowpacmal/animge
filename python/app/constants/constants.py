# Standard
from pathlib import Path

# Third-party
from huggingface_hub import repo_info
from platformdirs import user_documents_dir


# Private
_APP_NAME = "Animge"
_USER_DOCUMENTS_DIR = Path(user_documents_dir())


# Directory
CACHE_DIR = _USER_DOCUMENTS_DIR / _APP_NAME / "models"
TEMP_DIR = _USER_DOCUMENTS_DIR / _APP_NAME / "temp"

for dir in (CACHE_DIR, TEMP_DIR):
    dir.mkdir(parents=True, exist_ok=True)


# Hugging Face
_MODEL_NAME = "animagine-xl-4.0"
REPO_ID = f"cagliostrolab/{_MODEL_NAME}"

_REPO_INFO = repo_info(repo_id=REPO_ID, files_metadata=True)
_REPO_FILES_TO_DOWNLOAD = [
    f for f in _REPO_INFO.siblings or [] if not f.rfilename.startswith(_MODEL_NAME)
]
REPO_TOTAL_SIZE = sum(f.size or 0 for f in _REPO_FILES_TO_DOWNLOAD)
