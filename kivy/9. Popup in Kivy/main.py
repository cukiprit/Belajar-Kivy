from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class WidgetsLayout(Widget):
    def btn(self):
        show_popup()

class PopUps(FloatLayout):
    pass

class PopUpsApp(App):
    def build(self):
        return WidgetsLayout()

def show_popup():
    show = PopUps()

    popupWindow = Popup(
        title="Pop Up Window",
        content=show,
        size_hint=(None, None),
        size=(200, 200)
    )
    popupWindow.open()

PopUpsApp().run()