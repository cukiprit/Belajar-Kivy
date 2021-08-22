from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class Background(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass

class SampleBackgroundApp(App):
    def build(self):
        return Background()

SampleBackgroundApp().run()