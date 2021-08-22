from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout

class Text_input(Widget):
    pass

class MainInputApp(App):
    def build(self):
        return Text_input()

    def text_process(self):
        text = self.root.ids.Input.text
        print(text)

MainInputApp().run()