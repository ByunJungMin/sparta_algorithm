# 최빈값 구하기2

input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26                            # 길이가 26이고 모든 인덱스값이 0인 배열 선언

    for char in string:                                             
        if not char.isalpha():                                      # char 이 문자열이 아닌지 확인
            continue
        arr_index = ord(char) - ord('a')                            # ord() 로 아스키코드 변환 후 arr_index 에 저장
        alphabet_occurrence_array[arr_index] += 1                   # alphabet_ ~ 배열에 arr_index번째 인덱스에 + 1
    
    max_occurrence = 0                                        
    max_alphabet_index = 0                                      
                                                           
    for index in range(len(alphabet_occurrence_array)):             # alphabet_occurrence_ ~ 배열의 길이를 객체로 변환 하여 반복문 실행
                                                                
        alphabet_occurrence = alphabet_occurrence_array[index]      # alphabet_occurrence_ ~ 의 [index] 번째 값 저장 
    
        if alphabet_occurrence > max_occurrence:                    # 크기 비교
            max_alphabet_index = index                              # 최대값 저장
            max_occurrence = alphabet_occurrence                    
                                                                
    
    return chr(max_alphabet_index + ord('a'))                       # chr() 로 아스키코드를 문자로 반환



result = find_max_occurred_alphabet(input)
print(result)