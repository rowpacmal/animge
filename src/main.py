import flet as ft


from layouts import AppFooter, AppHeader, AppMain


def main(page: ft.Page):
    # Page
    page.title = "Animge"
    page.theme_mode = ft.ThemeMode.DARK

    # Window
    page.window.maximized = True
    page.window.min_width = 1024
    page.window.min_height = 768
    page.window.center()

    # Styles
    page.padding = 0

    # UI
    page.appbar = AppHeader()
    page.bottom_appbar = AppFooter()

    page.add(AppMain())


ft.app(main)
