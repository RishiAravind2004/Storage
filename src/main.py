import flet as ft
from flet_geolocator import Geolocator, GeolocatorSettings, GeolocatorPositionAccuracy

def view(page: ft.Page):
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(title=ft.Text("Geolocator Demo"))

    # UI text fields
    permission_text = ft.Text("🔓 Permission: --")
    position_text = ft.Text("📡 Current Position: --")
    last_known_text = ft.Text("🕘 Last Known Position: --")
    status_text = ft.Text("🔍 Permission Status: --")
    gps_status_text = ft.Text("📶 GPS Enabled: --")
    error_text = ft.Text("", color=ft.Colors.RED)

    def on_position_change(e):
        position_text.value = f"📍 New Position: {e.latitude}, {e.longitude}"
        page.update()

    def on_error(e):
        error_text.value = f"❌ Error: {e.data}"
        page.update()

    gl = Geolocator(
        location_settings=GeolocatorSettings(accuracy=GeolocatorPositionAccuracy.BEST),
        on_position_change=on_position_change,
        on_error=on_error
    )
    page.overlay.append(gl)

    # Button handlers (non-async)
    def handle_permission(e):
        try:
            res = gl.request_permission()
            permission_text.value = f"🔓 Permission: {res}"
        except Exception as ex:
            error_text.value = f"❌ Permission Error: {ex}"
        page.update()

    def handle_current_position(e):
        try:
            pos = gl.get_current_position()
            position_text.value = f"📡 Current Position: {pos.latitude}, {pos.longitude}"
        except Exception as ex:
            error_text.value = f"❌ Location Error: {ex}"
        page.update()

    def handle_last_known(e):
        try:
            pos = gl.get_last_known_position()
            if pos:
                last_known_text.value = f"🕘 Last Known Position: {pos.latitude}, {pos.longitude}"
            else:
                last_known_text.value = "🕘 Last Known Position: Not available"
        except Exception as ex:
            error_text.value = f"❌ Last Known Error: {ex}"
        page.update()

    def handle_status(e):
        try:
            status = gl.get_permission_status()
            status_text.value = f"🔍 Permission Status: {status}"
        except Exception as ex:
            error_text.value = f"❌ Status Error: {ex}"
        page.update()

    def check_gps_enabled(e):
        try:
            enabled = gl.is_location_service_enabled()
            gps_status_text.value = f"📶 GPS Enabled: {'✅ Yes' if enabled else '❌ No'}"
        except Exception as ex:
            gps_status_text.value = f"❌ GPS Error: {ex}"
        page.update()

    def open_app_settings(e):
        try:
            gl.open_app_settings()
        except Exception as ex:
            error_text.value = f"❌ App Settings Error: {ex}"
        page.update()

    def open_location_settings(e):
        try:
            gl.open_location_settings()
        except Exception as ex:
            error_text.value = f"❌ Location Settings Error: {ex}"
        page.update()

    # UI layout
    page.add(
        ft.Column([
            ft.OutlinedButton("📶 Check GPS Enabled", on_click=check_gps_enabled),
            ft.OutlinedButton("🔓 Request Permission", on_click=handle_permission),
            ft.OutlinedButton("📡 Get Current Position", on_click=handle_current_position),
            ft.OutlinedButton("🕘 Get Last Known Position", on_click=handle_last_known),
            ft.OutlinedButton("🔍 Get Permission Status", on_click=handle_status),
            ft.OutlinedButton("⚙️ Open App Settings", on_click=open_app_settings),
            ft.OutlinedButton("📍 Open Location Settings", on_click=open_location_settings),
            gps_status_text,
            permission_text,
            position_text,
            last_known_text,
            status_text,
            error_text,
        ])
    )

ft.app(target=view)
