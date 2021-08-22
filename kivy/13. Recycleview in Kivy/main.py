from kivy.app import App
from kivy.uix.recycleview import RecycleView

class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]

class RecycleApp(App):
    def build(self):
        return ExampleViewer()

RecycleApp().run()