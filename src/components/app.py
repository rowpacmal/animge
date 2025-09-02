# Core
import flet as ft

# Local
from layouts import AppFooter, AppHeader, AppMain


class App(ft.Container):
    def __init__(self):
        super().__init__()

        # Styles
        self.alignment = ft.alignment.center
        self.expand = True

        # UI
        self.content = ft.Column(
            controls=[AppHeader(), AppMain(), AppFooter()],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
