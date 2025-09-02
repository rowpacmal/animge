import flet as ft


class ProgressBar(ft.ProgressBar):
    def __init__(self, value=0):
        super().__init__()

        # Styles
        self.height = 20
        self.width = 600
        self.border_radius = 20

        # States
        self.value = value
