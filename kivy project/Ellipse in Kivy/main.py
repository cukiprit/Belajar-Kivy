from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class EllipseKivy(GridLayout):
    pass

class EllipseKivyApp(App):
    def build(self):
        return EllipseKivy()

EllipseKivyApp().run()