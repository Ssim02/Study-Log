# 백준 4153번 - 직각삼각형

## 문제 링크
- [백준 4153번 - 직각삼각형] (https://www.acmicpc.net/problem/4153)

## 문제 요약
- 삼각형의 세 변의 길이가 주어진다. 그 삼각형이 직각삼각형인지 아닌지를 출력하는 문제

## 풀이 요약
- 입력받은 세 변중에 어떤 게 빗변인지를 판단한다. 리스트에 세 변을 넣고, 입력받은 세 값 중 가장 큰 값을 리스트에서 제거한다. 리스트에 남은 두 요소가 자연히 빗변을 제외한 나머지 두 변일 것이므로, (빗변**2 = 나머지변1**2 + 나머지변2**2)을 풀어 직각삼각형인지 아닌지를 출력했다.

## 최종 코드
    # 백준 4153번 - 직각삼각형

    while True :
        # 입력
        h, b, p = map(int, input().split())
        # 어떤 게 빗변인지를 판단
        h_judgment = []
        h_judgment.append(h)
        h_judgment.append(b)
        h_judgment.append(p)
        max = h_judgment[0]
        for i in range(3) :
            if h_judgment[i] > max :
                max = h_judgment[i]
        # 종료 조건
        if h == 0 and b == 0 and p == 0 :
            break
        # h값을 제거해 나머지 b, p를 정의할 수 있도록
        h_judgment.remove(max)
        # h_judgment에 남은 요소는 두개가 됨(각각 b, p가 됨)
        # 직각삼각형인지를 판단
        if (max**2) == (h_judgment[0]**2) + (h_judgment[1]**2) :
            print("right")
        else :
            print("wrong")

