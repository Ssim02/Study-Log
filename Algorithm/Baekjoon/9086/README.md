# 백준 9086번 - 문자열

## 문제 링크
- [백준 9086번 - 문자열] (https://www.acmicpc.net/problem/9086)

## 문제 요약
- 입력으로 주어진 문자열의 첫 글자와 마지막 글자를 출력하는 문제

## 풀이 아이디어
- 입력받은 문자열의 첫 글자와 마지막 글자를 인덱스를 통해 접근해서 출력했다.

## 최종 코드
    # 백준 9086번 - 문자열

    test_case = int(input())

    for i in range(test_case) :
        word = list(input())
        first = word[0]
        last = word[-1]
        print(first+last)


