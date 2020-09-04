"""
INI ファイルを参照して 
API 呼び出し～ JSON ファイルへの書き込みができるか確かめるテスト
"""
import configparser
import json

import requests


config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8")

API_KEY = config_ini["Key"]["APIKEY"]
ZIP = config_ini["Zip"]["ZIP"]
API_URL = "http://api.openweathermap.org/data/2.5/forecast?zip={0},jp&units=metric&APPID={1}"

url = API_URL.format(ZIP, API_KEY)


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

print("***\n" + str(jsn["list"][0]["weather"][0]["description"]) + "\n***\n")