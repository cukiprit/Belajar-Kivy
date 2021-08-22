from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout

class CustomDropDown(DropDown):
    pass

class DropDownLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(DropDownLayout, self).__init__(**kwargs)
        
        self.dropdown = CustomDropDown()
        self.mainButton = Button(
            text='Apakah kamu sedang kuliah?',
            size_hint_x=0.6,
            size_hint_y=0.15
        )

        self.add_widget(self.mainButton)
        self.mainButton.bind(on_release=self.dropdown.open)

        self.dropdown.bind(
            on_select=lambda\
                instance, x: setattr(self.mainButton, 'text', x)
        )

        self.dropdown.bind(on_select=self.callback)

    def callback(self, instance, x):
        print(f"Mode yang dipilih adalah {x}")

class DropDownApp(App):
    def build(self):
        return DropDownLayout()

DropDownApp().run()