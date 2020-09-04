#! python3.7
# -*- coding: utf-8 -*-
"""
メイン画面の設置、INI ファイルを参照しての API 呼び出し ～ JSON ファイルへの書き込み、
何時に処理を回すかの設定(動作未チェック)(2020/09/04時点)
"""
import configparser
import json

import requests
import schedule
from kivy.app import App
from kivy.config import Config
from kivy.core.text import DEFAULT_FONT, LabelBase
from kivy.resources import resource_add_path
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 568)
Config.set('graphics', 'resizable', 0)

resource_add_path(r'.\fonts')
LabelBase.register(DEFAULT_FONT, r'fonts\mplus-2c-regular.ttf')

config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8")

API_KEY = config_ini["Key"]["APIKEY"]
ZIP = config_ini["Zip"]["ZIP"]
API_URL = "http://api.openweathermap.org/data/2.5/forecast?zip={0},jp&units=metric&APPID={1}"

url = API_URL.format(ZIP, API_KEY)


def get_weatherworecast():
    """
    天気情報を取得するやつ
    """
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

schedule.every().day.at("21:14").do(get_weatherworecast)

def select_word():
    """
    ここに言葉を選ぶためのチャートプログラムを入れるか、 
    別ファイルに書いたものをimport して入れるか
    
    """


class Mainscreen(BoxLayout):
    str_src = StringProperty('')
    def __init__(self, **kwargs):
        super(Mainscreen, self).__init__(**kwargs)
        with open("tenkidata.json", "r") as f:
            jsn = json.load(f)
        self.str_src = str(jsn["list"][0]["weather"][0]["description"])

"""class Message(Label):
    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)
        with open("tenkidata.json", "r") as f:
            jsn = json.load(f)
        self.text = str(jsn["list"][0]["weather"][0]["description"])
"""

class GraphicApp(App):
    def __init__(self, **kwargs):
        super(GraphicApp, self).__init__(**kwargs)
        self.title = 'てんきよほう'
    def build(self):
        return Mainscreen()

if __name__ == "__main__":
    app = GraphicApp()
    app.run()
