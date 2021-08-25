from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class ButtonWidget(Widget):
    def callback(self, instance):
        print("Tombol telah ditekan")
        print(f"Tombol {instance} dengan state {instance.state}")

class ButtonApp(App):
    def build(self):
        return ButtonWidget()

if __name__ == "__main__":
    ButtonApp().run()