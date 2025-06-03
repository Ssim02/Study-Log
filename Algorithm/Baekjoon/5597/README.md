# 백준 5597번 - 과제 안 내신 분..?

## 문제 링크
[백준 5597번 - 과제 안 내신 분..?] (https://www.acmicpc.net/problem/5597)

## 문제 요약
- 1~30까지의 수 중, 입력으로 들어온 28개의 숫자가 아닌 나머지 두 수를 작은수부터 큰 수 순서로 출력하는 문제.

## 풀이 아이디어
- 1~30이 들어있는 리스트를 만들고, 입력이 하나 들어올 때마다 리스트에서 제거한다. 그 후 입력이 끝나면, 리스트에 남아있을 두 수를 출력한다.

## 최종 코드
    # 백준 5597번 - 과제 안 내신 분..?

    # 1~30이 저장된 리스트 만들기
    attendance_number = []
    for i in range(30) :
        attendance_number.append(i + 1)

    # 입력 받고, 입력받은 수를 리스트에서 제거
    for i in range(28) :
        n = int(input())
        if(n in attendance_number) :
            attendance_number.remove(n) 


    # 입력되지 않은 나머지 두 수 출력
    print(attendance_number[0])
    print(attendance_number[1])

