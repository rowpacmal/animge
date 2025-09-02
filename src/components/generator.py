# Core
import flet as ft

from contexts.contexts import app_contexts


class Generator(ft.Column):
    def __init__(self):
        super().__init__()

        # States
        self.visible = False

        # UI
        self.controls = [
            ft.Text("Generator"),
        ]

    def before_update(self):
        if app_contexts.is_ready and not self.visible:
            self.visible = True
