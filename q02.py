salList = []
salTotal = 0
print("-"*30)
print("{:^24}".format("員工薪資輸入"))
print("{:^19}".format("若姓名處未輸入則代表結束"))
print("-"*30)
while(True):
    name = input("請輸入姓名: ")
    if name == "":
        break
    else: 
        salary = int(input("請輸入薪資: "))
        salDict = {"ename":name,"esalary":salary}
    
    salList.append(salDict)
print("-"*30)
for i in range(len(salList)):
    print(f"員工{salList[i]['ename']} 的薪資為 {salList[i]['esalary']}")
    salTotal = salTotal + salList[i]['esalary']
salAve = round(salTotal/len(salList),2)
print("-"*30)
print("合計薪資為: ","{:>10}".format(salTotal))
print("平均薪資為: ","{:>10}".format(salAve))
