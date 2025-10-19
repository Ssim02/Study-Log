# 백준 8958번 - OX퀴즈

## 문제 링크
- [백준 8958번 - OX퀴즈] (https://www.acmicpc.net/problem/8958)

# 문제 요약
- "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 주어진다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제가지 연속된 O의 개수가 된다. 예를 들면, "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.이 경우 주어진 OX퀴즈에 따른 점수를 구하는 프로그램. 

## 풀이 아이디어
- O를 만날 때마다 늘어날 점수 변수(score)와, 하나의 테스트 케이스의 결과 점수를 저장할 변수(total_score)를 만든다.
주어진 OX퀴즈의 결과 중, O를 만나면 score += 1로 점수를 계산하고, total_score에 값을 더한다. X를 만나면 score = 0으로 초기화 시켜 점수를 구한다. 하나의 퀴즈 결과의 점수 계산이 끝나면, total_score를 출력한다. 하나의 퀴즈의 점수 계산이 끝나면, 두 변수를 초기화한 후 다음 퀴즈의 점수를 계산한다. 

## 최종 코드
    # 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
    # "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점

    # test case
    test_case_len = int(input())
    test_case = []


    for i in range(test_case_len) :
        ox = str(input())
        test_case.append(ox)

    # score calculate
    for calc in test_case :
        # score count
        score = 0 # O를 만날 때마다 증가할 값. X만나면 초기화
        total_score = 0 # 하나의 test_case의 점수. 출력할 값
        for i in calc :
            if i == "X" :
                score = 0
            if i == "O" :
                score += 1
                total_score += score
        print(total_score)





