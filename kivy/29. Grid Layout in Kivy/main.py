from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Grid_Layout(GridLayout):
    pass

class GridLayoutApp(App):
    def build(self):
        return Grid_Layout()

GridLayoutApp().run()