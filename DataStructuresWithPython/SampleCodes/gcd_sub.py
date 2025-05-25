# 최대공약수 구하기 - 뺄셈으로


def gcd(a, b) :
    while a != 0 and b != 0 :
        if a > b : 
            a = a - b
        else :
            b = b - a
    return a + b # 연산 끝나면 둘 중 하나는 0이 될 것이므로 

print(gcd(2, 10))
