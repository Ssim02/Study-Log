# 백준 2920 - 음계
# 연주한 순서가 주어졌을 때, ascending, descending, mixed인지 구분

# 연주한 순서 입력받기
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

interval = list(map(int, input().split()))

if interval == ascending :
    print("ascending")
elif interval == descending :
    print("descending")
else :
    print("mixed")

