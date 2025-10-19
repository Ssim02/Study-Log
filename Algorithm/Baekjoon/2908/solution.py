# 백준 2908 - 상수

# 두 수 입력
A, B = map(str, input().split())
new_A = []
new_B = []
# 수 뒤집기
for i in range(1, 4) :
    new_A.append(A[-i])
    new_B.append(B[-i])

newnew_A = new_A[0]+ new_A[1] + new_A[2]
newnew_B = new_B[0] + new_B[1] + new_B[2]
# 출력

if int(newnew_A) > int(newnew_B) :
    print(newnew_A)
else :
    print(newnew_B)



