# Core
import flet as ft


class AppFooter(ft.BottomAppBar):
    def __init__(self):
        super().__init__()

        # Styles
        self.bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST
        self.height = 40
        self.padding = 10

        # Content
        self.content = ft.Row(
            controls=[ft.Text("© 2025 Animge", size=15)],
            alignment=ft.MainAxisAlignment.CENTER,
        )
