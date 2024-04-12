l = int(input("몇 단까지 출력할까요?"))
for i in range(1, l + 1):
    print(f"-----[{i}단]-----")
    for j in range(1, 20):
        result = i * j
        print(f"{i} x {j} = {result}")
