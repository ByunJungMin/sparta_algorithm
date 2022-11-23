# 문자열 뒤집기 모두 0으로 만드는 횟수와 1로 만드는 횟수중 가장 작은 횟수 구하기


input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':                                # string의 0번째 인덱스가 0이면
        count_to_all_one += 1                           # count ~ _one + 1
    elif string[0] == '1':                              # string의 0번째 인덱스가 1이면
        count_to_all_zero += 1                          # count ~ _zero + 1

    for i in range(len(string) - 1):                    # string 의 길이만큼 반복
        if string[i] != string[i + 1]:                  # string의 i번째 인덱스와 string의 i+1번째 인덱스의 값이 같지 않고
            if string[i + 1] == '0':                    # string의 i + 1번째 인덱스가 0 이면
                count_to_all_one += 1                   # count ~ _one + 1  
            if string[i + 1] == '1':                    # string의 i + 1번째 인덱스가 1이면
                count_to_all_zero += 1                  # count ~ _zero + 1

    return min(count_to_all_one, count_to_all_zero)     # 0으로 만드는 횟수와 1로 만드는 횟수 둘중 최소의 횟수


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)