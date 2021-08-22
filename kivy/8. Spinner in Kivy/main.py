from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class SampleBoxLayout(FloatLayout):
    def spinner_clicked(self, value):
        print(f"Bahasa yang dipilih adalah {value}")

class SampleBoxApp(App):
    def build(self):
        Window.clearcolor = (0.555, 0.261, .888, 0.5)
        return SampleBoxLayout()

SampleBoxApp().run()