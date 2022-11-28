# 선택 정렬

input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):                      # 하나 남은 인덱스는 비교하지 않는다.
        min_index = i
        for j in range(n - i):                  # 1개씩 줄어들면서 비교하기 때문에 n - i
            if array[i + j] < array[min_index]: 
                min_index = i + j               # 01234 1234 234 34 식으로 반복하기 위해 i + j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!