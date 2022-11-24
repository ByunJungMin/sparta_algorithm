# 재귀함수

def count_down(number):
    if number < 0:         
        return
    print(number)          
    count_down(number - 1) # count_down 의 숫자를 -1 반복


count_down(60)