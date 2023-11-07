import pkg.modu
from pprint import PrettyPrinter
MENU_FILE = 'C:/Users/94202/Desktop/Scripting_Midterm/Scripting_Midterm/menu.json'       
OUTPUT_FILE = 'C:/Users/94202/Desktop/Scripting_Midterm/Scripting_Midterm/output.json'

menuDict = pkg.modu.read_json(MENU_FILE)
pkg.modu.print_json(menuDict)
discount = float(input("請輸入折扣: "))
pp = PrettyPrinter(indent=4,width=20)
menuDict = pkg.modu.process_data(menuDict,discount)
pkg.modu.print_json(menuDict)
pkg.modu.write_json(OUTPUT_FILE,menuDict)
