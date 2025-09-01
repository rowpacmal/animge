# Standard
import asyncio

# Core
import flet as ft

# Local
from .progress_bar import ProgressBar
from contexts import app_contexts
from utils import load_pretrained_model, track_download_progress


class ModelDownload(ft.Column):
    def __init__(self):
        super().__init__()

        # States
        self.is_downloading = False
        self.progress = 0
        self.tasks = []

        # UI
        self.progress_text = ft.Text(size=50)
        self.progress_bar = ProgressBar()
        self.controls = [
            self.progress_text,
            self.progress_bar,
        ]

    # Inherited
    def did_mount(self):
        assert self.page is not None

        self.is_downloading = True
        progress_task = self.page.run_task(self._update_progress)
        download_task = self.page.run_task(self._download_model)
        self.tasks.append(progress_task)
        self.tasks.append(download_task)

    def will_unmount(self):
        self.is_downloading = False
        for task in self.tasks:
            task.cancel()

    # Private
    async def _download_model(self):
        try:
            app_contexts.pipe = await asyncio.to_thread(
                load_pretrained_model,
            )
        except Exception as e:
            app_contexts.error = str(e)
        finally:
            self.is_downloading = False

    def _remove_ui(self):
        assert self.page is not None
        assert isinstance(self.parent, ft.Column)

        if self.parent:
            app_contexts.is_ready = True
            self.parent.controls.remove(self)
            self.page.update()

    async def _update_progress(self):
        await track_download_progress(
            on_update=self._update_ui,
            stop_flag=lambda: self.is_downloading,
            on_complete=self._remove_ui,
        )

    def _update_ui(self, progress, progress_text):
        self.progress = progress
        self.progress_text.value = progress_text
        self.progress_bar.value = progress / 100
        self.update()
