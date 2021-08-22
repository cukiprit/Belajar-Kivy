from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

class CheckBoxLayout(BoxLayout):
    def value_checkbox(self, instance, value):
        if value is True:
            print("Checkbox dipilih")
        else:
            print("Checkbox tidak dipilih")

class CheckBoxApp(App):
    def build(self):
        Window.clearcolor = (0, 0, .30, .60)
        return CheckBoxLayout()

CheckBoxApp().run()