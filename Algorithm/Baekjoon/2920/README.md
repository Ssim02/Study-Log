# 백준 2920번 - 음계 

## 문제 링크 
- [백준 2920번 - 음계] (https://www.acmicpc.net/problem/2920)

## 문제 요약
- 1부터 8까지 숫자가 주어졌을 때, 주어진 숫자가 ascending인지, descending인지, mixed인지 판별하는 프로그램을 만들어라. 

## 풀이 아이디어
- ascending과 desending은 숫자의 순서가 정해져있으므로, 미리 정해진 리스트를 만들어 놓고, 입력받은 숫자 리스트가 위 두 리스트와 일치하면 각각 asending과 desending으로 판별한다. 그 경우가 아닌 경우는 전부 mixed로 판별했다. 

## 최종 코드
    # 백준 2920 - 음계
    # 연주한 순서가 주어졌을 때, ascending, descending, mixed인지 구분

    # 연주한 순서 입력받기
    ascending = [1, 2, 3, 4, 5, 6, 7, 8]
    descending = [8, 7, 6, 5, 4, 3, 2, 1]

    interval = list(map(int, input().split()))

    if interval == ascending :
        print("ascending")
    elif interval == descending :
        print("descending")
    else :
        print("mixed")

