import random

def generate_lotto_numbers():
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    return f"생성된 로또 번호는 {(lotto_numbers)} 입니다."

print(generate_lotto_numbers())

