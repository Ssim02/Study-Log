# 백준 10872번 - 팩토리얼

## 문제 링크 
- [백준 10872번 - 팩토리얼] (https://www.acmicpc.net/problem/10872)

## 문제 요약
- 0보다 크거나 같은 정수 N이 주어 질 때, N!을 출력하는 프로그램을 작성하는 문제
## 풀이 아이디어
- 재귀함수를 사용해서 factorial함수를 구현했다. 0!과 1!이 같다는 점을 이용해서 탈출 조건을 n > 1이 아닐 때로 정해주었다. 
## 최종 코드
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

