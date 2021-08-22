from kivy.app import App
from kivy.uix.screenmanager import CardTransition, FadeTransition, FallOutTransition, RiseInTransition, ScreenManager, Screen, SlideTransition, SwapTransition, WipeTransition
from kivy.lang import Builder

Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        Button:
            text: 'Anda sekarang berada di layar 1 Pergi ke layar 2'
            background_color: 0, 0, 1, 1
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Layar 2'

<ScreenTwo>:
    BoxLayout:
        Button:
            text: 'Anda sekarang berada di layar 2 Pergi ke layar 3'
            background_color: 1, 1, 0, 1
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Layar 3'

<ScreenThree>:
    BoxLayout:
        Button:
            text: 'Anda sekarang berada di layar 3 Pergi ke layar 4'
            background_color: 1, 1, 1, 1
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Layar 4'

<ScreenFour>:
    BoxLayout:
        Button:
            text: 'Anda sekarang berada di layar 4 Pergi ke layar 5'
            background_color: 1, 0, 1, 1
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Layar 5'

<ScreenFive>:
    BoxLayout:
        Button:
            text: 'Anda sekarang berada di layar 5 Pergi ke layar 6'
            background_color: 1, 0, 0, 1
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Layar 6'

<ScreenSix>:
    BoxLayout:
        Button:
            text: 'Anda sekarang berada di layar 6 Pergi ke layar 1'
            background_color: 0, 0, 1, 1
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'Layar 1'
""")

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenFour(Screen):
    pass

class ScreenFive(Screen):
    pass

class ScreenSix(Screen):
    pass

# Macam-macam transisi di screen manager
# SlideTransition, CardTransition, SwapTransition, FadeTransition, FallOutTransition, RiseInTransition
# default transisi screen manager adalah SlideTransition

screen_manager = ScreenManager(transition=FadeTransition())

screen_manager.add_widget(ScreenOne(name="Layar 1"))
screen_manager.add_widget(ScreenTwo(name="Layar 2"))
screen_manager.add_widget(ScreenThree(name="Layar 3"))
screen_manager.add_widget(ScreenFour(name="Layar 4"))
screen_manager.add_widget(ScreenFive(name="Layar 5"))
screen_manager.add_widget(ScreenSix(name="Layar 6"))

class ScreenApp(App):
    def build(self):
        return screen_manager

ScreenApp().run()