class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

menu = {
    "커피": 3000,
    "녹차": 2500,
    "아이스티": 3000}

select = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
quantity = int(input("수량을 입력하세요: "))

if select in menu:
    beverage = Beverage(select, menu[select])
    total_price = beverage.calculate(quantity)
    print(f"총 가격은 {total_price}원 입니다.")

else:
    print("없는 메뉴 입니다.")
