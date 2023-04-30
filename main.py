# first example to be deployed in github as git static page
import flet as ft
def main(page: ft.Page):
    def add_handler(e):
        if not new_task.value: return
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    def keyboard_handler(event):
        if event.key == "Enter": add_handler(event)

    ## Αρχικοποίηση
    page.title = "Λίστα Καθηκόντων"
    new_task = ft.TextField(hint_text="Να μην ξεχάσω...", color="GRAY", width=250)
    page.add(ft.Row([new_task, ft.ElevatedButton(" + ", on_click=add_handler)]))

    page.on_keyboard_event = keyboard_handler

ft.app(target=main)