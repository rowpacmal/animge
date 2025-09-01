import flet as ft


class ProgressBar(ft.ProgressBar):
    def __init__(self, value=0):
        super().__init__()
        self.value = value
        self.border_radius = 20
        self.height = 20
