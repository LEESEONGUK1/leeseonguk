환율 = {"달러":1320,"엔":950,"위안":182}

보유 = [13, 200, 13]

a = 보유[0] * 환율["달러"]
b = 보유[1] * 환율["엔"]
c = 보유[2] * 환율["위안"]


x = "철수가 가지고 있는 돈의 원화 가치는"
y = (a+b+c)
z = "원 입니다."
print(x,y,z)

