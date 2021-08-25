from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class PageLayoutEx(PageLayout):
    pass

class PageLayoutApp(App):
    def build(self):
        return PageLayoutEx()

PageLayoutApp().run()