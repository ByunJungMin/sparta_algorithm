# 삽입 정렬

input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(1,5):                                                    # 첫번째 인덱스는 정렬이 되어있다는 가정 하에 1~4 까지 반복
        for j in range(i):                                                  # i가 늘어날 때 마다 비교하는 횟수도 같이 증가하기 때문에 i만큼 반복
            if array[i - j - 1] > array[i - j]:                             # array[0] > array[1] , array[1] > array[2] => array[0] > array[1] , ... 반복
                array[i - j -1], array[i - j] = array[i - j], array[i - j - 1]
            else:                                                           # 이미 정렬이 되어 있다면 break
                break
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!