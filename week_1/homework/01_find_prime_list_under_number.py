input = 20


def find_prime_list_under_number(number):
    prime_list = []                         # 소수를 담을 비어있는 배열

    for n in range(2, number + 1):          # 2 ~ number 까지의 길이
        for i in prime_list:            
            if n % i == 0 and i * i <= n:   # (i * i <= n)를 사용한 이유 n이 n의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는 조건이 필요하기 때문
                break
        else:
            prime_list.append(n)            # 배열에 소수를 추가

    return prime_list


result = find_prime_list_under_number(input)
print(result)