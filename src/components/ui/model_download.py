# Standard
import asyncio

# Core
import flet as ft

# Application
from .progress_bar import ProgressBar
from constants import CACHE_FOLDER, REPO_ID, MODEL_SIZE
from utils import get_folder_size, load_pretrained_model


class ModelDownload(ft.Column):
    def __init__(self):
        super().__init__()
        self.downloading = False
        self.progress = 0
        self.total_size = MODEL_SIZE
        self.alignment = ft.MainAxisAlignment.CENTER

        self.pipe = None
        self.tasks = []

        self.progress_text = ft.Text(value="0.00% (0.00 GB)", size=50)
        self.progress_bar = ProgressBar()

        self.controls = [
            self.progress_text,
            self.progress_bar,
        ]

    def did_mount(self):
        assert self.page is not None

        self.downloading = True
        download_task = self.page.run_task(self.update_progress)
        progress_task = self.page.run_task(self.download_model)
        self.tasks.append(download_task)
        self.tasks.append(progress_task)

    def will_unmount(self):
        self.downloading = False
        for task in self.tasks:
            task.cancel()

    async def download_model(self):
        self.pipe = await asyncio.to_thread(
            load_pretrained_model,
        )
        self.downloading = False

    async def update_progress(self):
        assert self.page is not None
        assert isinstance(self.parent, ft.Column)

        while True:
            current_size = get_folder_size(
                str(CACHE_FOLDER / f"models--{REPO_ID.replace('/', '--')}")
            )
            self.progress = min((current_size / self.total_size) * 100, 100)

            self.progress_text.value = (
                f"{self.progress:.2f}% ({self.total_size / 1024**3:.2f} GB)"
            )
            self.progress_bar.value = self.progress / 100
            self.update()

            if self.progress >= 100 and self.downloading is False:
                if self.parent:
                    self.parent.controls.remove(self)
                    self.page.update()
                break

            await asyncio.sleep(1)
