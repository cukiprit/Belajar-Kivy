from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class Anchor_Layout(GridLayout):
    pass

class AnchorLayoutApp(App):
    def build(self):
        return Anchor_Layout()

AnchorLayoutApp().run()