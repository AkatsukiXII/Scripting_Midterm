import pkg.modu
A1,A2 = input("請輸入頂點A座標: ").split(",")
B1,B2 = input("請輸入頂點B座標: ").split(",")
C1,C2 = input("請輸入頂點C座標: ").split(",")
vertexA = (A1,A2)
vertexB = (B1,B2)
vertexC = (C1,C2)
ans = pkg.modu.triangle_zhonxin(int(vertexA[0]),int(vertexB[0]),int(vertexC[0]),int(vertexA[1]),int(vertexB[1]),int(vertexC[1]))
print(f"此三角形的重心為: {ans}")
