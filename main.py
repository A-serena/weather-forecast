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
# import keisan
#from kivy.utils import platform

# from kivy.uix.widget import Widget


Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 568)
Config.set('graphics', 'resizable', 0)

resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, r'fonts\mplus-2c-regular.ttf')

class Mainscreen(BoxLayout):
    pass
    #text = StringProperty()    # プロパティの追加
    #def __init__(self, **kwargs):
    #    super(TextWidget, self).__init__(**kwargs)
    #    self.text = ''

config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8")


API_KEY = config_ini["Key"]["APIKEY"]
ZIP = config_ini["Zip"]["ZIP"]
API_URL = "http://api.openweathermap.org/data/2.5/forecast?zip={0},jp&units=metric&APPID={1}"

url = API_URL.format(ZIP, API_KEY)

def getWeatherForecast():
    response = requests.get(url)
    # forecastData = json.loads(response.text)
    data = response.json()

    # json の書き込み
    with open("tenkidata.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    with open("tenkidata.json", "r") as f:
        jsn = json.load(f)
    
    print(jsn)
    print("URLです。" + url)





class GraphicApp(App):
    def build(self):
        self.title = 'てんきよほう'
        return Mainscreen()
        getWeatherForecast()

if __name__ == "__main__":
    GraphicApp().run()
