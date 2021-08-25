from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.lang.builder import Builder

# you can change the file name if you want to see the different orientation or you can just change it
# in .kv orientation
Builder.load_file('bt-rl.kv')

class StackLayoutEx(StackLayout):
    pass

class StackApp(App):
    def build(self):
        return StackLayoutEx()

StackApp().run()