import json

obj = ["2", "efefa\narfwef"]
json.dump(obj, open("testEscape.json", "w+"))
