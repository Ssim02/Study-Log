# 백준 30802번 - 웰컴 키트

## 문제 링크
- [백준 30802번 - 웰컴 키트] (https://www.acmicpc.net/problem/30802)

## 문제 요약
- 주어진 조건을 만족하는 키트를 주문 할 때, 티셔츠를 최소 몇 묶음을 주문해야 하는지, 펜을 최대 몇 묶음 주문 가능한지, 그때 펜을 한 자루 씩 몇 개 주문하는지를 출력하는 문제

## 풀이 아이디어
    1. 입력값들을 모두 입력받아 저장한다
    2. 주문할 티셔츠의 묶음 수는 (각 사이즈의 신청자 수) // (몇장씩 주문할 것인지(T))의 값에 1을 더해서 구한다(0 or 정수 값이 나올 텐데, 0이면 1묶음, 정수 값이 나오면 티셔츠를 더 주문해야 하는 것이므로). 단, 신청자 수와 T값이 동일하면 정수값이 나오지만 더 주문해야 하는 것이 아니므로, if문에서 따로 처리해서 +1을 하지 않도록 처리하였다.
    3. 계산한 값들을 모두 출력한다. 
    
## 최종 코드
    import sys

    # 참가자의 수 N 입력
    N = int(sys.stdin.readline().rstrip())

    # 티셔츠 사이즈별 신청자의 수 입력
    # 순서는 S, M, L, XL, XXL, XXXL 순
    number_of_each_tshirt_size = list(map(int, sys.stdin.readline().rstrip().split()))

    # 정수 티셔츠와 펜의 묶음 수 입력
    T, P = sys.stdin.readline().rstrip().split()

    # 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지
    min_tshrit_bundle = 0
    for i in number_of_each_tshirt_size :
        # S~ XXXL사이즈까지 루프를 돌아 각 사이즈별로 몇 묶음을 주문해야 하는 지 계산
        # i = 각 사이즈별 신청자의 수
    
        temp = i // int(T) # 만약 신청자 수가 T의 배수라면 +1을 하면 안됨
        if i  % int(T) == 0 :
            min_tshrit_bundle += temp
        else :
            min_tshrit_bundle += (temp + 1)  

    # 펜을 P자루 씩 최대 몇 묶음 주문할 수 있는지와, 펜을 한 자루 씩 몇 개 주문해야 하는 지 계산

    max_pen_bundle = int(N // int(P)) # 최대 몇 묶음 주문 할 수 있는지
    each_pen = int(N % int(P)) # 한 자루씩 몇 개 주문해야 하는지

    # 출력부
    print(min_tshrit_bundle)
    print("{} {}".format(max_pen_bundle, each_pen))

