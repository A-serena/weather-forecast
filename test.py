import japanize_kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Mainscreen(BoxLayout):
    pass

class GraphicApp(App):
    def build(self):
        self.title = 'てんきよほう'
        return Mainscreen()
        
GraphicApp().run()