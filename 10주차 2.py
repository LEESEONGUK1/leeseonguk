import random
def making_lotto_numbers():
    lotto_numbers = random(range(1, 46), 6)
    lotto_numbers.sort()
    return f"생성된 로또 번호는 {','.join(map(str, lotto_numbers))} 입니다."

    print(making_lotto_numbers)