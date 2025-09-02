# Core
import flet as ft


class AppFooter(ft.Row):
    def __init__(self):
        super().__init__()

        # UI
        self.controls = [
            ft.Text(value="Footer", size=20),
        ]
