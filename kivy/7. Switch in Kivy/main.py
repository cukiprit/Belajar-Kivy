from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class SwitchLayout(GridLayout):
    rows = 4

    def switch_callback(self, switchObject, switchValue):
        if(switchValue):
            print("Switch dinyalakan")
        else:
            print("Switch dimatikan")

class SwitchApp(App):
    def build(self):
        return SwitchLayout()

SwitchApp().run()