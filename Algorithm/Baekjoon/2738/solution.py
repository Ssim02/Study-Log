# N, M 입력받기

N, M = map(int, input().split())

# A 행렬 입력받기
A = []
for i in range(N) :
    A.append(list(map(int, input().split())))

# B 행렬 입력받기
B = []
for i in range(N) :
    B.append(list(map(int, input().split())))

# 행렬 덧셈
for i in range(N) :
    for j in range(M) :
        print(A[i][j] + B[i][j], end=' ')
    print()   
