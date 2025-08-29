import flet as ft

class Counter:
  def __init__(self, initial_count=0):
    self.count = initial_count
    self.counter_text = ft.Text(str(self.count), size=50)
    self.fab = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.increment)

  def increment(self, e):
    self.count += 1
    self.counter_text.value = str(self.count)
    self.counter_text.update()

  def get_widgets(self):
    return self.counter_text, self.fab