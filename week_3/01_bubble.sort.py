# 버블 정렬

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n-1):            # 배열의 길이      
        for j in range(n - i -1):   # 마지막 인덱스에는 항상 최대값이 오기 때문에 비교하지 않기 위해 n - i - 1 길이만큼 반복
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1],array[j]      # j번째 인덱스와 j+1번째 인덱스 값을 서로 교체
    return


bubble_sort(input)
print(input)  