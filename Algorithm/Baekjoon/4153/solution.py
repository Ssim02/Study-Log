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

