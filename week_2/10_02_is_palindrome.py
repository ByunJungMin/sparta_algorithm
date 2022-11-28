# 재귀함수 회문

input = "소주만병만주소"


def is_palindrome(string):
    if len(string) <= 1:                # 글자가 하나여도 회문이므로 True 출력
        return True
    if string[0] != string[-1]:         # 맨앞글자와 맨뒷글자가 다르다면 False 출력
        return False
    return is_palindrome(string[1:-1])  # 소주만병만주소 > 주만병만주 > 만병만 > 병 의 순서


print(is_palindrome(input))