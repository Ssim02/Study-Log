# 백준 1259번 - 팰린드롬수

## 문제 링크
- [백준 1259번 - 팰린드롬수] (https://www.acmicpc.net/problem/1259)

## 문제 요약
- 어떤 수를 뒤에서부터 읽어도 똑같은 수를 팰린드롬수라고 한다. 주어진 입력이 팰린드롬수이면 yes, 아니면 no를 출력하는 문제이다. 입력으로 0이 들어오면 프로그램을 종료한다.(0은 팰린드롬수 판별에 포함되지 않는다)

## 풀이 아이디어
    1. 주어진 입력을 리스트에 저장한다.
    2. 그 리스트를 뒤에서부터 접근하여, 처음 입력과 같은지 비교한다.
    3. 같다면 yes, 다르다면 no를 출력한다.

## 최종 코드
    # 백준 1259번 - 팰린드롬수

    while True :
        n = list(map(int, input()))

        # 종료 조건
        if n[0] == 0 :
            break

        reversed_n = []
        
        # 주어진 입력을 뒤집어 새로운 리스트에 저장
        for i in reversed(n) :
            reversed_n.append(i)

        if n == reversed_n :
            print("yes")
        else :
            print("no")
