# 백준 9086번 - 문자열

test_case = int(input())

for i in range(test_case) :
    word = list(input())
    first = word[0]
    last = word[-1]
    print(first+last)

