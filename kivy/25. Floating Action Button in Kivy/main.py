from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class Base(BoxLayout):
    pass

class FloatingActionButtonApp(App):
    def build(self):
        return Base()

FloatingActionButtonApp().run()