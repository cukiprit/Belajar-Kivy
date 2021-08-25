from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class Base(RelativeLayout):
    pass

class ButtonApp(App):
    def build(self):
        return Base()

ButtonApp().run()