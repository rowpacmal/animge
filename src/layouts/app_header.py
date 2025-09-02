# Core
import flet as ft


class AppHeader(ft.Row):
    def __init__(self):
        super().__init__()

        # UI
        self.controls = [
            ft.Text(value="Animge", size=30, weight=ft.FontWeight.BOLD),
        ]
