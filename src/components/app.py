import flet as ft

from components.ui import Counter

class App:
  def __init__(self, page: ft.Page):
    self.page = page
    self.counter = Counter()
    
    counter_text, counter_fab_inc, counter_fab_dec = self.counter.get_widgets()
    self.page.add(ft.SafeArea(
            ft.Row(
                [
                  ft.Container(
                      counter_fab_dec,
                  ),
                  ft.Container(
                      counter_text,
                      width=200,
                      alignment=ft.alignment.center,
                  ),
                  ft.Container(
                      counter_fab_inc,
                  ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            expand=True,
        ))