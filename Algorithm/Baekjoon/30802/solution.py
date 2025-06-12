import sys

# 참가자의 수 N 입력
N = int(sys.stdin.readline().rstrip())

# 티셔츠 사이즈별 신청자의 수 입력
# 순서는 S, M, L, XL, XXL, XXXL 순
number_of_each_tshirt_size = list(map(int, sys.stdin.readline().rstrip().split()))

# 정수 티셔츠와 펜의 묶음 수 입력
T, P = sys.stdin.readline().rstrip().split()

# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지
min_tshrit_bundle = 0
for i in number_of_each_tshirt_size :
    # S~ XXXL사이즈까지 루프를 돌아 각 사이즈별로 몇 묶음을 주문해야 하는 지 계산
    # i = 각 사이즈별 신청자의 수
 
    temp = i // int(T) # 만약 신청자 수가 T의 배수라면 +1을 하면 안됨
    if i  % int(T) == 0 :
        min_tshrit_bundle += temp
    else :
        min_tshrit_bundle += (temp + 1)  

# 펜을 P자루 씩 최대 몇 묶음 주문할 수 있는지와, 펜을 한 자루 씩 몇 개 주문해야 하는 지 계산

max_pen_bundle = int(N // int(P)) # 최대 몇 묶음 주문 할 수 있는지
each_pen = int(N % int(P)) # 한 자루씩 몇 개 주문해야 하는지

# 출력부
print(min_tshrit_bundle)
print("{} {}".format(max_pen_bundle, each_pen))

