import json
from pprint import PrettyPrinter

with open ('C:/Users/94202/Desktop/Scripting_Midterm/Scripting_Midterm/menu.json','r',encoding = 'UTF-8') as f:
    menuDict = json.load(f)
print(type(menuDict),"\n")
pp = PrettyPrinter(indent=4,width=20)
#pp.pprint(menuDict)

inputDict = {
    "name": "海鮮燉飯",
    "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
}
menuDict["categories"][1]['items'].append(inputDict)
menuDict["categories"][1]['items'][2]['price'] = menuDict["categories"][1]['items'][2]['price']*0.9
pp.pprint(menuDict)
