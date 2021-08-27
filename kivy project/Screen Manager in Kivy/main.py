from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('Layout.kv')

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenFour(Screen):
    pass

class RootScreen(ScreenManager):
    pass

class ScreenManagerApp(App):
    def build(self):
        return RootScreen()

if __name__ == '__main__':
    ScreenManagerApp().run()