import flet as ft

from components import App


def main(page: ft.Page):
    # Page
    page.title = "Animge"

    # Window
    page.window.maximized = True
    page.window.min_width = 1024
    page.window.min_height = 768
    page.window.center()

    # Styles
    page.padding = 0

    # UI
    page.add(App())


ft.app(main)
