#! python3.7
# -*- coding: utf-8 -*-

import configparser
import json

import requests
from kivy.app import App
from kivy.config import Config
from kivy.core.text import DEFAULT_FONT, LabelBase
from kivy.resources import resource_add_path
from kivy.uix.boxlayout import BoxLayout
#from kivy.utils import platform

# from kivy.uix.widget import Widget


Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 568)
Config.set('graphics', 'resizable', 0)

resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, 'fonts\mplus-2c-regular.ttf')

class Mainscreen(BoxLayout):
    pass
    #text = StringProperty()    # プロパティの追加
    #def __init__(self, **kwargs):
    #    super(TextWidget, self).__init__(**kwargs)
    #    self.text = ''

config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8")

city_name = "Utsunomiya"

API_KEY = config_ini["Key"]["APIKEY"]
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

url = api.format(city=city_name, key=API_KEY)
print(url)

response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)
# json の書き込み
with open("tenkidata.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


class GraphicApp(App):
    def build(self):
        self.title = 'てんきよほう'
        return Mainscreen()

if __name__ == "__main__":
    GraphicApp().run()
