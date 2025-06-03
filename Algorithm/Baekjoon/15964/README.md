# 백준 15964 - 이상한 기호

## 문제 링크
- [백준 15964번 - 이상한 기호] (https://www.acmicpc.net/problem/15964)

## 문제 요약
- 새로운 연산자를 정의하고, 그 연산자를 이용한 계산을 출력하는 문제.

## 풀이 아이디어
- 문제에서 주어진 연산을 정의하는 새로운 연산을 가지는 함수를 만들어 해결했다.

## 최종 코드
    # 백준 15964 - 이상한 기호

    def sub(a, b) :
        res = (a+b)*(a-b)
        return res


    a, b = map(int, input().split())

    print(sub(a, b))

