from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class Base(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return Base()

MainApp().run()