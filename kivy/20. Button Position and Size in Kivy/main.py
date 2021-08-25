from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class ButtonFloatLayout(FloatLayout):
    pass

class ButtonApp(App):
    def build(self):
        return ButtonFloatLayout()

ButtonApp().run()