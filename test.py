import flet as ft
from flet import margin

def Greetings_Page():
    return ft.View(
        route="/greetings",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        # Greeting Title
                        ft.Text(
                            "Welcome to BumbleBeeZ🐝",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "Where Empathy Meets Innovation 💛",
                            italic=True,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),

                        # Greeting Message
                        ft.Text(
                            "BumbleBeeZ is more than just an app — it's a movement.",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "We’re here to empower people with disabilities, the elderly, and orphans by providing "
                            "accessible tools, personalized support, and a community that cares. "
                            "Just like the bumblebee, we believe in achieving the impossible — together. 🐝✨",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        
                        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),

                        # Register / Login Buttons
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Register",
                                    icon=ft.Icons.PERSON_ADD,
                                    on_click=lambda e: e.page.go("/register"),
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.Colors.GREEN,
                                        color=ft.Colors.WHITE,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        padding=10,
                                    )
                                ),
                                ft.ElevatedButton(
                                    "Login",
                                    icon=ft.Icons.LOGIN,
                                    on_click=lambda e: e.page.go("/login"),
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.Colors.BLUE,
                                        color=ft.Colors.WHITE,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        padding=10,
                                    )
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                        ),
                        ft.Text(
                            "New to BumbleBeeZ? Start your journey by registering.",
                            text_align=ft.TextAlign.CENTER,
                            size=12,
                            italic=True,
                            color=ft.Colors.GREY,
                        ),
                    ],
                    spacing=20,
                    scroll=ft.ScrollMode.ADAPTIVE,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                image=ft.DecorationImage(
                    src="https://raw.githubusercontent.com/RishiAravind2004/Storage/main/icon.png",
                    opacity=0.1,
                    fit=ft.ImageFit.COVER,
                ),
                expand=True,
                alignment=ft.alignment.center,
                padding=20,
            ),
        ]
    )
