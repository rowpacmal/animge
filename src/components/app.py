# Core
import flet as ft

# Local
from layouts import AppFooter, AppHeader, AppMain


class App:
    def __init__(self, page: ft.Page):
        self.page = page

        # Page
        self.page.title = "Animagine"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Styles
        self.page.padding = 0

        # Window
        self.page.window.maximized = True
        self.page.window.min_width = 1024
        self.page.window.min_height = 768
        self.page.window.center()

        # UI
        self.page.add(
            ft.Column(
                controls=[AppHeader(), AppMain(), AppFooter()],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        )
