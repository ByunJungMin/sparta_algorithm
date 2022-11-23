# 이진 탐색
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0                                     # finding_numbers 의 최솟값
    current_max = len(array) - 1                        # finding_numbers 의 최대값
    current_guess = (current_min + current_max) // 2    # 최솟값 + 최대값 // 2 (/를 두번 씀으로써 나머지 제외) 즉 중간값

    while current_min <= current_max:
        if array[current_guess] == target:              # target 이 중간값과 동일하다면
            return True
        elif array[current_guess] < target:             # 중간값이 target 보다 작다면
            current_min = current_guess + 1             # 최솟값에 중간값 + 1 저장
        else:
            current_max = current_guess - 1             # 중간값이 target 보다 크다면 최대값에 중간값 - 1 저장
        current_guess = (current_min + current_max) // 2 # 최솟값과 최대값의 중간값 저장 
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)