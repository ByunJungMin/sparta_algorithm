# 반복되지 않는 문자중 첫번째 문자 반환 만약 그런문자가 없으면 "_" 반환

input = "abadabac"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26                             

    for char in string:                                                 
        if not char.isalpha():                                            
            continue
        arr_index = ord(char) - ord('a')                           
        alphabet_occurrence_array[arr_index] += 1                       

    not_repeating_character_array = []                                     
    for index in range(len(alphabet_occurrence_array)):                      
        alphabet_occurrence = alphabet_occurrence_array[index]            
        if alphabet_occurrence == 1:                                         
            not_repeating_character_array.append(chr(index + ord('a')))    

    for char in string:                                                  
        if char in not_repeating_character_array:                             
            return char
    
    return '_'

result = find_not_repeating_character(input)
print(result)

