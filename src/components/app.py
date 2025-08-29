import flet as ft

from components.ui import Counter

class App:
  def __init__(self, page: ft.Page):
    self.page = page
    self.counter = Counter()
    
    counter_text, counter_fab = self.counter.get_widgets()
    self.page.floating_action_button = counter_fab
    self.page.add(ft.SafeArea(
            ft.Container(
                counter_text,
                alignment=ft.alignment.center,
            ),
            expand=True,
        ))