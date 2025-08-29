import flet as ft

from components import App
from contexts import app_context


def main(page: ft.Page):
    print("App: ", app_context.app)
    App(page)


ft.app(main)
