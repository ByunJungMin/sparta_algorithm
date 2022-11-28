# 재귀함수 회문

input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):                         
        if string[i] != string[n - 1 - i]:      # string의 첫번째 인덱스와 마지막 인덱스 비교
            return False                        # 0 과 4, 1 과 3 같이 인덱스가 같이 변해야 하기 때문에 [n - 1 - i] 사용
        
        
    return True


print(is_palindrome(input))