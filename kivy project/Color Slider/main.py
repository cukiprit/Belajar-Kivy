from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SliderColorWidget(BoxLayout):
    pass

class SliderApp(App):
    def build(self):
        return SliderColorWidget()

if __name__ == '__main__':
    SliderApp().run()