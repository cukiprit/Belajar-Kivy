from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class Base(FloatLayout):
    pass

class ButtonApp(App):
    def build(self):
        return Base()

ButtonApp().run()