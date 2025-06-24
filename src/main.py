import flet as ft
import flet_geolocator as fg

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(title=ft.Text("Geolocator Demo"))

    # Status display texts
    permission_text = ft.Text("🔓 Permission: --")
    position_text = ft.Text("📍 Position: --")
    error_text = ft.Text("❌ Error: --")

    page.add(permission_text, position_text, error_text)

    # Callback: Update when location changes
    def on_position_change(e):
        position_text.value = f"📍 Position: {e.latitude}, {e.longitude}"
        position_text.update()

    # Callback: Update on error
    def on_error(e):
        error_text.value = f"❌ Error: {e.data}"
        error_text.update()

    # Create Geolocator and add to overlay BEFORE using
    geo = fg.Geolocator(
        on_position_change=on_position_change,
        on_error=on_error
    )
    page.overlay.append(geo)

    # Async handler for permission request
    async def handle_request_permission():
        result = await geo.request_permission_async()
        permission_text.value = f"🔓 Permission: {result}"
        permission_text.update()

    # Start listening to location (optional)
    # await geo.start_position_updates_async()

    page.add(
        ft.ElevatedButton("Request Permission", on_click=lambda e: page.run_task(handle_request_permission))
    )

ft.app(target=main)
