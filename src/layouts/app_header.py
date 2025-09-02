# Core
import flet as ft


class AppHeader(ft.AppBar):
    def __init__(self):
        super().__init__()

        # Leading
        self.leading = ft.Icon(ft.Icons.AUTO_AWESOME_ROUNDED, size=40)
        self.leading_width = 30

        # Title
        self.title = ft.Text(
            "Animge", size=30, font_family="Roboto", weight=ft.FontWeight.BOLD
        )
        self.center_title = False

        # Styles
        self.color = ft.Colors.ON_PRIMARY
        self.bgcolor = ft.Colors.ON_PRIMARY_CONTAINER

        # UI
        self.theme_button = ft.IconButton(
            ft.Icons.DARK_MODE, on_click=self._toggle_theme
        )

        # Actions
        self.actions = [
            self.theme_button,
            ft.PopupMenuButton(
                icon=ft.Icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.ON_SURFACE),
                                ft.Text("Settings"),
                            ]
                        )
                    ),
                ],
            ),
        ]

    def _toggle_theme(self, e):
        assert self.page is not None
        self.page.theme_mode = (
            ft.ThemeMode.LIGHT
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        self.theme_button.icon = (
            ft.Icons.DARK_MODE
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.Icons.LIGHT_MODE
        )
        self.page.update()
