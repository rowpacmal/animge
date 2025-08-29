import flet as ft

from contexts import app_contexts


class Counter:
    def __init__(self):
        self.counter_text = ft.Text(str(app_contexts.counter.count), size=50)
        self.fab_inc = ft.FloatingActionButton(
            icon=ft.Icons.ADD, on_click=self.increment
        )
        self.fab_dec = ft.FloatingActionButton(
            icon=ft.Icons.REMOVE, on_click=self.decrement
        )

        app_contexts.counter.subscribe(self.update_widgets)

    def increment(self, e):
        app_contexts.counter.increment()

    def decrement(self, e):
        app_contexts.counter.decrement()

    def update_widgets(self):
        self.counter_text.value = str(app_contexts.counter.count)
        self.counter_text.update()

    def get_widgets(self):
        return self.counter_text, self.fab_inc, self.fab_dec
