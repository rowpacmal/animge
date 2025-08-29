import flet as ft


def main(page: ft.Page):
    count = 0
    counter = ft.Text(str(count), size=50)

    def increment_click(e):
        nonlocal count
        count += 1
        counter.value = str(count)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
