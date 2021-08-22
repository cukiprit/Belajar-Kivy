from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SliderWidget(BoxLayout):
    pass

class SliderApp(App):
    def build(self):
        return SliderWidget()

SliderApp().run()