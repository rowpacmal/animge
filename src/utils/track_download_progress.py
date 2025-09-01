# Standard
import asyncio
from pathlib import Path

# Local
from .get_folder_size import get_folder_size
from constants import CACHE_FOLDER, REPO_ID, REPO_SIZE


async def track_download_progress(on_update, stop_flag, on_complete):
    while True:
        folder_path = CACHE_FOLDER / f"models--{REPO_ID.replace('/', '--')}"
        current_size = get_folder_size(folder_path=folder_path)
        progress = min((current_size / REPO_SIZE) * 100, 100)
        progress_text = f"{progress:.2f}% ({current_size / 1024**3:.2f} GB / {REPO_SIZE / 1024**3:.2f} GB)"
        on_update(progress, progress_text)

        if round(progress, 2) >= 100 and stop_flag():
            on_complete()
            break

        await asyncio.sleep(1)
