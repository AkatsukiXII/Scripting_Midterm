import json
from pprint import PrettyPrinter


def triangle_zhonxin(x1,x2,x3,y1,y2,y3):
    int(x1,x2,x3,y1,y2,y3)
    xans = round((x1+x2+x3)/3)
    yans = round((y1+y2+y3)/3)
    ans = (xans,yans)
    return ans

def read_json(menuFile):
    with open (menuFile,'r',encoding = 'UTF-8') as f:
        menuDict = json.load(f)
    return menuDict

def process_data(menuDict,discount):
    inputDict = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
    menuDict["categories"][1]['items'].append(inputDict)
    for i in range(2):
        menuDict["categories"][0]['items'][i]['price'] = round(menuDict["categories"][0]['items'][i]['price']*discount)
    for i in range(3):
        menuDict["categories"][1]['items'][i]['price'] =  round(menuDict["categories"][1]['items'][i]['price']*discount)
    return menuDict

def print_json(menuDict):
    menuJson = json.dumps(menuDict,ensure_ascii=False,indent=4)
    print(menuJson)
    
def write_json(outputFile,menuDict):
    with open (outputFile,'w',encoding = 'UTF-8') as f:
        json.dump(menuDict,f,ensure_ascii=False,indent=4)