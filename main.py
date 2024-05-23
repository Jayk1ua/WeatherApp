from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

class WeatherCard(MDCard):
    def __init__(self, *args, **kwarsg):
        super().__init__(*args, **kwarsg)


class MainScreen(MDScreen):
    def __init__(self, *args, **kwarsg):
        super().__init__(*args, **kwarsg)

class WeatherApp(MDApp):
    def build(self):
        Builder.load_file('style.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.screen = MainScreen("MainScreen")
        return self.screen


WeatherApp().run()