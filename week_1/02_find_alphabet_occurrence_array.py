# 알파벳을 아스키코드로 변환하고 배열에 저장


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26            # alphabet_ ~ 이름의 변수에 길이가 26이고 모든 인덱스값이 0 인 배열 선언

    for char in string:                                 
        if not char.isalpha():                      # .isalpha = 문자열인지 확인 
            continue
        arr_index = ord(char) - ord('a')            # ord = 아스키 코드로 변환 
        alphabet_occurrence_array[arr_index] += 1 

    return alphabet_occurrence_array
    

print(find_alphabet_occurrence_array("hello my name is sparta"))


