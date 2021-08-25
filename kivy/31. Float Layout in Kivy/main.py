from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class FloatLayoutEx(FloatLayout):
    pass

class FloatLayoutApp(App):
    def build(self):
        return FloatLayoutEx()

FloatLayoutApp().run()