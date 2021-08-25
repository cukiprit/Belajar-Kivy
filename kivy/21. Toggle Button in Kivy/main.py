from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton

class ToggleButtonLayout(GridLayout):
    pass

class ToggleApp(App):
    def build(self):
        return ToggleButtonLayout()

ToggleApp().run()