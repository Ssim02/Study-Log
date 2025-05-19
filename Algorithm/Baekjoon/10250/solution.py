# 백준 10250번 - ACM 호텔

# 테스트 케이스 입력받기
test_case = int(input())

for i in range(test_case) :
    h, w, n = map(int, input().split())
    # N번째 손님에게 배정되어야 하는 방 번호 출력
    floor = n % h
    room = n // h + 1
    if floor == 0 :
        floor = h
        room -= 1

    print("{0}{1:02d}".format(floor, room))
