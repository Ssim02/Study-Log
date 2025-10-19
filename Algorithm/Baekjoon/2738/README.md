# 백준 2738번 - 행렬 덧셈

## 문제 링크
- [백준 2738번 - 행렬 덧셈](https://www.acmicpc.net/problem/2738)

## 문제 요약
- N*M크기의 두 행렬 A, B가 주어졌을 때, 두 행렬을 더하는 프로그램
## 풀이 아이디어
- 각 행렬을 2차원 리스트로 입력받고, 각 행렬의 원소를 인덱스를 통해 접근해 더해 출력했다.
## 최종 코드
    # N, M 입력받기

    N, M = map(int, input().split())

    # A 행렬 입력받기
    A = []
    for i in range(N) :
        A.append(list(map(int, input().split())))

    # B 행렬 입력받기
    B = []
    for i in range(N) :
        B.append(list(map(int, input().split())))

    # 행렬 덧셈
    for i in range(N) :
        for j in range(M) :
            print(A[i][j] + B[i][j], end=' ')
        print()   
