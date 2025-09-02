# Core
import flet as ft

# Local
from components.ui import Generator, ModelDownload


class AppMain(ft.Column):
    def __init__(self):
        super().__init__()

        # Styles
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True

        # UI
        self.controls = [
            ModelDownload(),
            Generator(),
        ]
