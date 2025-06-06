# 백준 2908번 - 상수

## 문제 링크
- [백준 2908번 - 상수] (https://www.acmicpc.net/problem/2908)
## 문제 요약
- 입력받은 수를 뒤집은 수를 비교해 뒤집은 수 중 더 큰 수를 출력하는 문제

## 풀이 아이디어
- 두 수를 입력받고, 인덱스를 뒤부터 접근해 새로운 수를 리스트에 넣는다. 그 후 수를 비교해서 더 큰 걸 출력한다.

## 최종 코드
    # 백준 2908 - 상수

    # 두 수 입력
    A, B = map(str, input().split())
    new_A = []
    new_B = []
    # 수 뒤집기
    for i in range(1, 4) :
        new_A.append(A[-i])
        new_B.append(B[-i])

    newnew_A = new_A[0]+ new_A[1] + new_A[2]
    newnew_B = new_B[0] + new_B[1] + new_B[2]
    # 출력

    if int(newnew_A) > int(newnew_B) :
        print(newnew_A)
    else :
        print(newnew_B)



