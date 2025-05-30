# 백준 10872번 - 팩토리얼
# N!을 출력하는 프로그램

n = int(input())

# 재귀함수로 구현
def factorial(n) :
    if n > 1 :
        return n * factorial(n-1)
    else :
        return 1

print(factorial(n))
