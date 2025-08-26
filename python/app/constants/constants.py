# Standard libraries
from pathlib import Path

# Third-party libraries
from platformdirs import user_documents_dir


# Private constants
_APP_NAME = "Animge"
_USER_DOCUMENTS_DIR = Path(user_documents_dir())

# Directory
CACHE_DIR = _USER_DOCUMENTS_DIR / _APP_NAME / "models"
TEMP_DIR = _USER_DOCUMENTS_DIR / _APP_NAME / "temp"

for dir in (CACHE_DIR, TEMP_DIR):
    dir.mkdir(parents=True, exist_ok=True)

# Model
MODEL_ID = "cagliostrolab/animagine-xl-4.0"
