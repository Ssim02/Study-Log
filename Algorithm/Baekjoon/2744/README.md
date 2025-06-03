# 백준 2744번 - 대소문자 바꾸기

## 문제 링크
- [백준 2744번 - 대소문자 바꾸기] (https://www.acmicpc.net/problem/2744)

## 문제 요약
- 주어진 문자열을 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 문제

## 풀이 아이디어
- isupper, islower을 이용해 대문자인지 소문자인지 검사하고, upper, lower을 사용해 변환해 출력했다.

## 최종 코드
    # 백준 2744번 - 대소문자 바꾸기

    # 입력
    word = input()
    # 바꾼 결과를 저장할 문자열
    res = ''
    # 대소문자 변환
    for i in word :
        if i.isupper() :
            res += i.lower()
        if i.islower() :
            res += i.upper()
    # 출력
    print(res)

