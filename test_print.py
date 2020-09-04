import json

with open("tenkidata.json", "r") as f:
    jsn = json.load(f)

print("***\n" + str(jsn["list"][0]["weather"][0]["description"]) + "\n***\n")