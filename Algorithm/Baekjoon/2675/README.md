# 백준 2675번 - 문자열 반복

## 문제 링크 
- [백준 2675번 - 문자열 반복] (https://www.acmicpc.net/problem/2675)

## 문제 요약
- 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램

## 풀이 아이디어
- 입력받은 문자열의 인덱스를 이용해 입력받은 반복횟수만큼 곱해서 출력

## 최종 코드

    # 테스트 케이스 입력받기
    test_case_number= int(input())
    r_array = []
    s_array = []

    for i in range(test_case_number) :
        r, s = input().split() # 반복횟수 r과 문자열 s을 공백을 기준으로 입력받음
        r_array.append(r) #
        s_array.append(s)

    # i번째 문자 r번 반복 출력
    for i in range(len(r_array)) :
        for sub_i in s_array[i] :
            print(sub_i * int(r_array[i]), end = "") # 줄바꿈 생략
        print() # 다음 test case 구분 위해 줄바꿈꿈
 