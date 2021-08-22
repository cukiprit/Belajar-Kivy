from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

class CanvasWidget(ButtonBehavior, Label):
    pass

class CanvasWidgetApp(App):
    def build(self):
        return CanvasWidget()

CanvasWidgetApp().run()