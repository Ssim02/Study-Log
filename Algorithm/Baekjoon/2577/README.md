#  백준 2577번 - 숫자의 개수

## 문제 링크
- [백준 2577번 - 숫자의 개수] (https://www.acmicpc.net/problem/2577)

## 문제 요약
- 세 개의 자연수가 주어질 때 세 자연수를 곱한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램

## 풀이 아이디어
- 각각의 숫자를 키로 하는 딕셔너리를 생성해 숫자가 각각 몇 번 쓰였는지를 카운트


## 최종 코드
a = int(input())
b = int(input())
c = int(input())

res = a * b * c

str_res = str(res)

res_dict = {
    "0" : 0,
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0,
}

for i in str_res :
    if i in res_dict :
        res_dict[i] += 1

for i in res_dict :
    print(res_dict[i])