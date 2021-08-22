from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout

class ProgressBarLayout(BoxLayout):
    pass

class ProgressBarApp(App):
    def build(self):
        return ProgressBarLayout()

ProgressBarApp().run()