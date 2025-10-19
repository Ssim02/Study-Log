# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램

# 정수의 개수 N 입력받기
N = int(input())

# 공백으로 구분된 정수 입력받기
n = map(int, input().split())
print(list(n))

# 찾으려고 하는 정수 v 입력받기
v = int(input())

count = 0
# N개의 정수 중 v가 몇 개인지를 구하기
for i in n :
    if v == i :
        count += 1
        print("up")

print(count)
