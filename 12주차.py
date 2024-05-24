class Bun:
    def __init__(self, name, price):
        self.contents = name
        self.price = price
        self.total_sales = 0

    def sell(self):
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        self.total_sales += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

cream_bun = Bun(name="슈크림", price=1000)
pat_bun = Bun(name="팥", price=1000)

cream_bun.sell()
pat_bun.sell()

print(f"총 판매금: {cream_bun.total_sales + pat_bun.total_sales}원")
