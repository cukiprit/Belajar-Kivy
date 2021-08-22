from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# membuat class root widget yang akan kita gunakan di file .kv
class KivyBoxLayout(BoxLayout):
    pass

class KivyBoxLayoutApp(App):
    # return instance dari class KivyBoxLayout()
    def build(self):
        return KivyBoxLayout()

KivyBoxLayoutApp().run()