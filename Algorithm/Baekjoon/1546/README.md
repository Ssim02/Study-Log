# 백준 1546번 - 평균

## 문제 링크
- [백준 1546번 - 평균] (https://www.acmicpc.net/problem/1546)

## 문제 요약
- 점수들을 받는다. 그 중 최고 점수를 M이라고 한다. 그 후 모든 점수를 점수/M*100으로 고친다. 모든 점수를 위 방식대로 고쳤을 때, 새로운 평균을 구하는 프로그램을 작성하는 문제이다. 

## 풀이 아이디어
- 입력받은 성적을 주어진 조건에 맞추어 새로운 성적으로 바꾸어 리스트에 저장한다. 그리고 그 리스트의 요소들을 모두 더하고, 주어진 성적의 수로 나누어 새로운 평균을 구해 출력한다. 

## 최종 코드
    # 백준 1546번 - 평균

    # 시험을 본 과목의 개수 N 입력
    N = int(input())

    # 현재 성적을 입력
    now_score_list = list(map(int, input().split()))
    new_score_list = [] # 새로운 성적을 저장할 리스트

    # 성적 중 최고점을 구하기
    max_score = 0
    for i in now_score_list :
        if i > max_score :
            max_score = i   


    # 새로운 점수 구하기
    for i in now_score_list :
        new_score_list.append(i / max_score * 100)

    # 새로운 평균 구하기
    avg = 0
    for i in new_score_list :
        avg += i

    # 새로 구한 평균을 출력
    print(avg/len(now_score_list))

        