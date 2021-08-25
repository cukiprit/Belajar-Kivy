from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class RelativeLayoutEx(RelativeLayout):
    pass

class RelativeLayoutApp(App):
    def build(self):
        return RelativeLayoutEx()

RelativeLayoutApp().run()