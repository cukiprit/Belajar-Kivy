from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config

class ButtonRelativeLayout(RelativeLayout):
    pass

class ButtonApp(App):
    def build(self):
        return ButtonRelativeLayout()

ButtonApp().run()