def validate_resident_registration_number(resident_number):

    numbers = [int(char) for char in resident_number if char.isdigit()]
    multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    total = sum(num * mult for num, mult in zip(numbers[:-1], multipliers))
    remainder = total % 11
    result = 11 - remainder

    if result == numbers[-1]:
        return True
    else:
        return False

resident_number = input("주민등록번호를 입력하세요 (예: YYMMDD-1234567): ")
if validate_resident_registration_number(resident_number):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
