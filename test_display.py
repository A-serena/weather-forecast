
"""
取得～書き込みの後の、
取った情報を指定した箇所に表示できるか確かめるテスト
"""
import json

from kivy.app import App
# from kivy.config import Config
# from kivy.core.text import DEFAULT_FONT, LabelBase
# from kivy.resources import resource_add_path
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 568)
Config.set('graphics', 'resizable', 0)

class Mainscreen(BoxLayout):
    str_src = StringProperty('')
    def __init__(self, **kwargs):
        super(Mainscreen, self).__init__(**kwargs)
        with open("tenkidata.json", "r") as f:
            jsn = json.load(f)
        self.str_src = str(jsn["list"][0]["weather"][0]["description"])

class GraphicApp(App):
    def __init__(self, **kwargs):
        super(GraphicApp, self).__init__(**kwargs)
        self.title = 'てんきよほう'
    def build(self):
        return Mainscreen()

if __name__ == "__main__":
    app = GraphicApp()
    app.run()