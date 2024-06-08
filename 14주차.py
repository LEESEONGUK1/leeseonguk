menu = ['냉면', '볶음밥', '피자', '짜장면']
while True:
    try:
        choice = input("메뉴를 선택해주세요 (1. 냉면, 2. 볶음밥, 3. 피자, 4. 짜장면): ")
        choice = int(choice)
        print("선택된 메뉴: " + menu[choice - 1])
        break

    except ValueError:
        print("숫자를 입력해주세요.")
    except IndexError:
        print("메뉴에 있는 번호를 입력해주세요.")
