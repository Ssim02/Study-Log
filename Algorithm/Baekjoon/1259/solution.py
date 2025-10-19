# 백준 1259번 - 팰린드롬수

while True :
    n = list(map(int, input()))

    # 종료 조건
    if n[0] == 0 :
        break

    reversed_n = []
    
    # 주어진 입력을 뒤집어 새로운 리스트에 저장
    for i in reversed(n) :
        reversed_n.append(i)

    if n == reversed_n :
        print("yes")
    else :
        print("no")
