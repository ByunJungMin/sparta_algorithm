# 병합정렬 merge

array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array_c = []                                                            # array_a 와 array_b 를 비교해서 작은 값을 array_C[] 에 저장
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):        # array1_index가 array1 배열의 길이보다 작고 array2_index가 array2 배열의 길이보다 작을 때 까지 반복
        if array1[array1_index] < array2[array2_index]:                     
            array_c.append(array1[array1_index])                            # array_c 에 작은값 입력
            array1_index += 1

        else:
            array_c.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):                                         # 만약 array1_index 가 array1 길이만큼 반복했다면
        while array2_index < len(array2):                                   
            array_c.append(array2[array2_index])                            # 남은 array2 배열을 array_C 에 입력
            array2_index += 1

    if array2_index == len(array2):                                         # 만약 array2_index 가 array2 길이만큼 반복했다면
        while array1_index < len(array1):                   
            array_c.append(array1[array1_index])                            # 남은 array1 배열을 array_C 에 입력
            array1_index += 1
    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!