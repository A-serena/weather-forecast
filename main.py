import json
from kivy.config import Config
Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 568)
Config.set('graphics', 'resizable', 0)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
import requests

resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf')

city_name = "Utsunomiya"
API_KEY = "39077ee91b12be0324841b9406a7024b"
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"


class Mainscreen(BoxLayout):
    pass
    #text = StringProperty()    # プロパティの追加
    #def __init__(self, **kwargs):
    #    super(TextWidget, self).__init__(**kwargs)
    #    self.text = ''


url = api.format(city=city_name, key=API_KEY)
print(url)

response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)
# json の書き込み
with open(r"C:\Users\User\Documents\py_kivy\TENKIYOHOU\tenkidata.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


class GraphicApp(App):
    def build(self):
        self.title = 'てんきよほう'
        return Mainscreen()

if __name__ == "__main__":
    GraphicApp().run()