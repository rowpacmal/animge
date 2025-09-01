# Core
import flet as ft

# Application
from components.ui import ModelDownload


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Animagine"
        self.page.padding = 0
        self.page.add(
            ft.Column(
                controls=[ModelDownload()],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )
        )
