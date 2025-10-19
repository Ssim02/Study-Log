# 백준 2754번 - 학점 계산

## 문제 링크
- [백준 2754번 - 학점 계산] (https://www.acmicpc.net/problem/2754)

## 문제 요약
- 어떤 성적이 주어졌을 때, 평점은 몇 점인지를 출력하는 문제

## 풀이 아이디어
- 주어진 모든 성적을 if문의 분기로 두어 저장된 평점이 나오도록 하였다.

## 최종 코드
    
    # 백준 2754번 - 학점계산
    # 첫째 줄에 성적이 주어짐
    grade = input()

    if grade == "A+" :
        print("4.3")
    elif grade == "A0" :
        print("4.0")
    elif grade == "A-" :
        print("3.7")
    elif grade == "B+" :
        print("3.3")
    elif grade == "B0" :
        print("3.0")
    elif grade == "B-" :
        print("2.7")
    elif grade == "C+" :
        print("2.3")
    elif grade == "C0" :
        print("2.0")
    elif grade == "C-" :
        print("1.7")
    elif grade == "D+" :
        print("1.3")
    elif grade == "D0" :
        print("1.0")
    elif grade == "D-" :
        print("0.7")
    elif grade == "F" :
        print("0.0")

