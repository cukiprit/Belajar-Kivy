from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class Base(FloatLayout):
    def __init__(self, **kwargs):
        super(Base, self).__init__(**kwargs)

    def say_hello(self):
        print("Hai Hello")

class ButtonApp(App):
    def build(self):
        return Base()

ButtonApp().run()