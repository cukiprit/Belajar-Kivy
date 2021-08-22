from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class ImageKivy(BoxLayout):
    pass

class ImageApp(App):
    def build(self):
        return ImageKivy()

ImageApp().run()