
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.03, 0.10, 1)

class FFPlayer(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        title = Label(
            text="FF AI PLAYER",
            font_size=30,
            bold=True,
            color=(0.1, 0.6, 1, 1)
        )
        layout.add_widget(title)

        subtitle = Label(
            text="AI SCREEN ANALYSIS",
            font_size=16
        )
        layout.add_widget(subtitle)

        for name in [
            "PLAYER LOGIN",
            "BATTLE ROYALE",
            "CLASH SQUAD",
            "LONE WOLF",
            "HEADSHOT TRAINING",
            "PLAYER STATS"
        ]:
            btn = Button(
                text=name,
                font_size=18,
                background_normal="",
                background_color=(0.05, 0.25, 0.55, 1)
            )
            btn.bind(
                on_press=lambda instance, n=name:
                self.select_mode(n)
            )
            layout.add_widget(btn)

        return layout

    def select_mode(self, name):
        print(name, "SELECTED")

FFPlayer().run()
