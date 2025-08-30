import flet as ft

from huggingface_hub import model_info
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
    StableDiffusionPipeline,
)

from pathlib import Path
import os
import asyncio


def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it's a symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


model_id = "cagliostrolab/animagine-xl-4.0"
documents_folder = (
    Path.home()
    / "Documents"
    / "Animge"
    / "models"
    / f"models--{model_id.replace('/', '--')}"
)
info = model_info(repo_id=model_id, files_metadata=True)
siblings = info.siblings or []
total_size = sum(f.size or 0 for f in siblings)
cache_folder = Path.cwd() / "storage" / ".cache"
# cache_folder = Path.home() / "Documents" / "Animge" / "models"
cache_folder.mkdir(parents=True, exist_ok=True)


class Download(ft.Column):
    def __init__(self):
        super().__init__()
        self.downloading = False
        self.progress = 0
        self.total_size = total_size
        self.alignment = ft.MainAxisAlignment.CENTER

        self.pipe = None
        self.tasks = []

        self.progress_text = ft.Text(value="0.00% (0.00 GB)", size=50)
        self.progress_bar = ft.ProgressBar(
            value=0, height=20, width=600, border_radius=10
        )

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
        print("Downloading model...")
        self.pipe = await asyncio.to_thread(
            StableDiffusionPipeline.from_pretrained,
            model_id,
            cache_dir=str(cache_folder),
        )
        print("DONE")
        self.downloading = False

    async def update_progress(self):
        while True:
            current_size = get_folder_size(
                str(cache_folder / f"models--{model_id.replace('/', '--')}")
            )
            self.progress = min((current_size / self.total_size) * 100, 100)

            self.progress_text.value = (
                f"{self.progress:.2f}% ({self.total_size / 1024**3:.2f} GB)"
            )
            self.progress_bar.value = self.progress / 100
            self.update()

            if self.progress >= 100 and self.downloading is False:
                break

            await asyncio.sleep(1)


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Animagine"
        self.page.padding = 0
        self.page.add(
            ft.Container(
                content=Download(),
                alignment=ft.alignment.center,
                expand=True,
            )
        )
