#  백준 1152번 - 단어의 개수

## 문제 링크
- [백준 1152번 - 단어의 개수] (https://www.acmicpc.net/problem/1152)

## 문제 요약
- 문자열이 주어졌을 때 그 문자열은 몇 개의 단어로 구성되어 있는지를 구하는 프로그램 

## 풀이 아이디어
- split()을 이용하여 입력받은 문자열을 단어로 쪼개서 단어의 개수를 카운트


## 최종 코드
count = 0 
s = input()
words= s.split()
for i in range(len(words)) :
    count += 1
print(count)