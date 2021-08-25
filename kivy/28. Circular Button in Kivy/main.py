from kivy.app import App
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class CircularButton(ButtonBehavior, Label):
    pass

class ButtonApp(App):
    def build(self):
        return CircularButton()

ButtonApp().run()