from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Login(GridLayout):
    pass

class LoginApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    LoginApp().run()