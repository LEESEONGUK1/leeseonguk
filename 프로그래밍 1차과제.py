#30개 야구장의 펜스 거리 데이터베이스, 딕셔너리
stadiums = {
#내셔널 리그
    "트루이스트 파크": {"left_field": 102, "deep_left_field": 117, "center_field":122, "deep_right_field": 114, "right_field": 99},
    "론디포 파크": {"left_field": 104, "deep_left_field": 117, "center_field":124, "deep_right_field": 119, "right_field": 102},
    "시티 필드": {"left_field": 109, "deep_left_field": 117, "center_field":124, "deep_right_field": 121, "right_field": 114},
    "시티즌스 뱅크 파크": {"left_field": 114, "deep_left_field": 125, "center_field":122, "deep_right_field": 112, "right_field": 101},
    "내셔널스 파크": {"left_field": 103, "deep_left_field": 115, "center_field":123, "deep_right_field": 113, "right_field": 102},
    "리글리 필드": {"left_field": 108, "deep_left_field": 112, "center_field":122, "deep_right_field": 122, "right_field": 107},
    "그레이트 아메리칸 볼파크": {"left_field": 100, "deep_left_field": 116, "center_field":123, "deep_right_field": 113, "right_field": 99},
    "아메리칸 패밀리 필드": {"left_field": 105, "deep_left_field": 113, "center_field":122, "deep_right_field": 114, "right_field": 105},
    "PNC 파크": {"left_field": 117, "deep_left_field": 125, "center_field":122, "deep_right_field": 114, "right_field": 98},
    "부시 스타디움": {"left_field": 102, "deep_left_field": 114, "center_field":122, "deep_right_field": 114, "right_field": 102},
    "체이스 필드": {"left_field": 114, "deep_left_field": 126, "center_field":124, "deep_right_field": 126, "right_field": 114},
    "쿠어스 필드": {"left_field": 100, "deep_left_field": 113, "center_field":120, "deep_right_field": 108, "right_field": 101},
    "다저 스타디움": {"left_field": 100, "deep_left_field": 114, "center_field": 120, "deep_right_field": 114, "right_field": 100},
    "펫코 파크": {"left_field": 109, "deep_left_field": 119, "center_field": 121, "deep_right_field": 119, "right_field": 110},
    "오라클 파크": {"left_field": 111, "deep_left_field": 122, "center_field": 119, "deep_right_field": 126, "right_field": 111},
#아메리칸 리그
    "캠든 야즈": {"left_field": 101, "deep_left_field": 114, "center_field": 125, "deep_right_field": 114, "right_field": 97},
    "펜웨이 파크": {"left_field": 95, "deep_left_field": 115, "center_field": 118, "deep_right_field": 115, "right_field": 92},
    "양키 스타디움": {"left_field": 97, "deep_left_field": 122, "center_field": 124, "deep_right_field": 117, "right_field": 96},
    "트로피카나 필드": {"left_field": 96, "deep_left_field": 110, "center_field": 123, "deep_right_field": 110, "right_field": 98},
    "로저스 센터": {"left_field": 100, "deep_left_field": 112, "center_field": 120, "deep_right_field": 112, "right_field": 100},
    "게런티드 레이트 필드": {"left_field": 101, "deep_left_field": 114, "center_field": 122, "deep_right_field": 114, "right_field": 102},
    "프로그레시브 필드": {"left_field": 99, "deep_left_field": 113, "center_field": 124, "deep_right_field": 114, "right_field": 99},
    "코메리카 파크": {"left_field": 105, "deep_left_field": 113, "center_field": 126, "deep_right_field": 111, "right_field": 101},
    "카우프만 스타디움": {"left_field": 101, "deep_left_field": 118, "center_field": 125, "deep_right_field": 118, "right_field": 101},
    "타깃 필드": {"left_field": 103, "deep_left_field": 115, "center_field": 124, "deep_right_field": 112, "right_field": 100},
    "미닛 메이드 파크": {"left_field": 105, "deep_left_field": 123, "center_field": 124, "deep_right_field": 124, "right_field": 105},
    "에인절 스타디움 오브 에너하임": {"left_field": 106, "deep_left_field": 118, "center_field": 120, "deep_right_field": 113, "right_field": 106},
    "링센트럴 콜리세움": {"left_field": 101, "deep_left_field": 112, "center_field": 122, "deep_right_field": 112, "right_field": 101},
    "T-모바일 파크": {"left_field": 101, "deep_left_field": 115, "center_field": 122, "deep_right_field": 116, "right_field": 99},
    "글로브 라이프 필드": {"left_field": 105, "deep_left_field": 125, "center_field": 124, "deep_right_field": 125, "right_field": 104},

}


def is_home_run(distance, direction, stadiums):
    """
    타구의 비거리와 방향을 입력받아, 메이저리그 30개 야구장 중 홈런이 될 수 있는지 판단하는 함수
    :param distance: 타구의 비거리 (미터)
    :param direction: 타구의 방향 ('left', 'deep left', 'center', 'deep right', 'right')
    :param stadiums: 야구장별 홈런 기준 정보
    :return: 홈런이 될 수 있는 야구장 리스트
    """
    home_run_stadiums = []
    for stadium, field in stadiums.items():
        if direction == 'left' and distance >= field['left_field']:
            home_run_stadiums.append(stadium)
        elif direction == 'deep left' and distance >= field['deep_left_field']:
            home_run_stadiums.append(stadium)
        elif direction == 'center' and distance >= field['center_field']:
            home_run_stadiums.append(stadium)
        elif direction == 'deep right' and distance >= field['deep_right_field']:
            home_run_stadiums.append(stadium)
        elif direction == 'right' and distance >= field['right_field']:
            home_run_stadiums.append(stadium)

    # 모든 야구장에서 홈런이 되는 경우 "*==NO DOUBT HOMERUN==*"출력
    if len(home_run_stadiums) == len(stadiums):
        return "*==NO DOUBT HOMERUN==*", home_run_stadiums
    return home_run_stadiums


# 사용자 입력
user_distance = float(input("타구의 비거리를 입력하세요 (미터): "))
user_direction = input("타구의 방향을 입력하세요 ('left', 'deep left', 'center', 'deep right', 'right'): ")

# 홈런 가능 야구장 출력
hr_result = is_home_run(user_distance, user_direction, stadiums)
if isinstance(hr_result, tuple):
    print(hr_result[0])

else:
    print(f"해당 타구는 {len(hr_result)}개의 야구장에서 홈런이 될 수 있습니다: {hr_result}")
