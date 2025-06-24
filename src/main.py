import flet as ft
import flet_geolocator as fg

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(title=ft.Text("Geolocator Tests"))

    # Define reusable Text widgets
    permission_status_text = ft.Text("🔓 Permission: --")
    position_status_text = ft.Text("📡 Position: --")
    service_status_text = ft.Text("⚙️ Service: --")
    error_text = ft.Text("❌ Error: --")

    page.add(permission_status_text, position_status_text, service_status_text, error_text)

    def handle_position_change(e):
        position_status_text.value = f"📡 Position: {e.latitude}, {e.longitude}"
        position_status_text.update()

    gl = fg.Geolocator(
        location_settings=fg.GeolocatorSettings(
            accuracy=fg.GeolocatorPositionAccuracy.LOW
        ),
        on_position_change=handle_position_change,
        on_error=lambda e: (
            setattr(error_text, "value", f"❌ Error: {e.data}"),
            error_text.update()
        ),
    )
    page.overlay.append(gl)

    def settings_dlg(handler):
        return ft.AlertDialog(
            adaptive=True,
            title=ft.Text("Opening Location Settings..."),
            content=ft.Text(
                "You are about to be redirected to the location/app settings. "
                "Please locate this app and grant it location permissions."
            ),
            actions=[ft.TextButton(text="Take me there", on_click=handler)],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )

    # Async handlers
    async def handle_permission_request():
        p = await gl.request_permission_async(wait_timeout=60)
        permission_status_text.value = f"🔓 Permission: {p}"
        permission_status_text.update()

    async def handle_get_permission_status():
        p = await gl.get_permission_status_async()
        permission_status_text.value = f"🔓 Permission: {p}"
        permission_status_text.update()

    async def handle_get_current_position():
        p = await gl.get_current_position_async()
        position_status_text.value = f"📡 Position: ({p.latitude}, {p.longitude})"
        position_status_text.update()

    async def handle_get_last_known_position():
        p = await gl.get_last_known_position_async()
        position_status_text.value = f"📡 Last Known: ({p.latitude}, {p.longitude})"
        position_status_text.update()

    async def handle_location_service_enabled():
        p = await gl.is_location_service_enabled_async()
        service_status_text.value = f"⚙️ Location Service Enabled: {p}"
        service_status_text.update()

    async def handle_open_location_settings():
        p = await gl.open_location_settings_async()
        page.close(location_settings_dlg)
        service_status_text.value = f"⚙️ Opened Location Settings: {p}"
        service_status_text.update()

    async def handle_open_app_settings():
        p = await gl.open_app_settings_async()
        page.close(app_settings_dlg)
        service_status_text.value = f"⚙️ Opened App Settings: {p}"
        service_status_text.update()

    location_settings_dlg = settings_dlg(lambda e: page.run_task(handle_open_location_settings))
    app_settings_dlg = settings_dlg(lambda e: page.run_task(handle_open_app_settings))

    # Buttons
    page.add(
        ft.Row(
            wrap=True,
            controls=[
                ft.OutlinedButton("Request Permission", on_click=lambda e: page.run_task(handle_permission_request)),
                ft.OutlinedButton("Get Permission Status", on_click=lambda e: page.run_task(handle_get_permission_status)),
                ft.OutlinedButton("Get Current Position", on_click=lambda e: page.run_task(handle_get_current_position)),
                ft.OutlinedButton(
                    "Get Last Known Position",
                    visible=not page.web,
                    on_click=lambda e: page.run_task(handle_get_last_known_position),
                ),
                ft.OutlinedButton("Is Location Service Enabled", on_click=lambda e: page.run_task(handle_location_service_enabled)),
                ft.OutlinedButton(
                    "Open Location Settings",
                    visible=not page.web,
                    on_click=lambda e: page.open(location_settings_dlg),
                ),
                ft.OutlinedButton(
                    "Open App Settings",
                    visible=not page.web,
                    on_click=lambda e: page.open(app_settings_dlg),
                ),
            ],
        )
    )

ft.app(target=main)
