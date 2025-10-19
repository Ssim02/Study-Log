# 백준 1676번 - 팩토리얼 0의 개수

## 문제 링크
- [백준 1676번 - 팩토리얼 0의 개수] (https://www.acmicpc.net/problem/1676)

## 문제 요약
- N!의 값에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구해 그 개수를 출력하는 문제

## 풀이 아이디어
    1. 먼저 N!의 값을 구한다.
    2. 구한 N!의 값을 리스트에 저장한다(reversed()를 사용해 역순으로 접근하기 위함)
    3. N!의 값을 역순으로 접근해, 0이 나오면 count_zero를 하나 증가시켜 0의 개수를 센다.
    4. 만약 0이 아닌 다른 것이 등장한다면, 현재 count_zero를 출력하고 루프를 종료시켜 프로그램을 끝낸다.
    
## 최종 코드
    # 백준 1676 - 팩토리얼 0의 개수

    # N!의 값을 구하고, 뒤에서부터 0의 개수를 센다(단, 0이 아닌 수가 처음으로 나오면 종료)

    N = int(input())

    def factorial(N) :
        if N == 0 or N == 1 :
            return 1
        else :
            return N * factorial(N - 1)

    # 팩토리얼 값을 역순으로 접근하여, 하나씩 검사해 처음으로 0이 아닌 수가 나오면 루프를 종료시키기
    prob = list(str(factorial(N))) # reversed()로 하나씩 접근 위해 리스트에 저장
    count_zero = 0
    for i in reversed(prob) : # 역순으로 접근
        if i == '0' : # 0이 등장하면 count_zero를 하나 증가시키기
            count_zero += 1
        else : # 처음으로 0이 아닌 수가 등장한 경우일 것 -> 현재 count_zero 출력하고 루프 종료
            print(count_zero)
            break

