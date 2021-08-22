from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.carousel import Carousel

class CarouselLayout(GridLayout):
    pass

class CarouselApp(App):
    def build(self):
        main = Carousel()

        for x in range(20):
            main.add_widget(CarouselLayout())
        
        return main

CarouselApp().run()