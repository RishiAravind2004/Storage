import flet as ft
import flet_geolocator as fg

def main(page: ft.Page):
    txt = ft.Text("Status: --")

    async def check_permission():
        geo = fg.Geolocator()
        result = await geo.request_permission_async()
        txt.value = f"Permission: {result}"
        txt.update()

    page.add(txt, ft.ElevatedButton("Request Permission", on_click=lambda e: page.run_task(check_permission)))

ft.app(target=main)
