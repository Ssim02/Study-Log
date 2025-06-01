# 백준 11718번 - 그대로 출력하기

## 문제 링크
- [백준 11718번 - 그대로 출력하기] (https://www.acmicpc.net/problem/11718)

## 문제 요약
- 입력 받은 그대로 출력하는 문제.

## 풀이 아이디어
- 예외 처리를 이용해서, EOFError가 발생하면(input이 더이상 없을 때), 즉 입력이 끝나면 종료하도록 했다. 

## 최종 코드
    # 백준 11718 - 그대로 출력하기
    # 예외 처리 이용해서 풀이
    while(True) :
        try :
            n = input()
            print(n)
        except EOFError:
            break
