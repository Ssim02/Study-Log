# 백준 8958번 - OX퀴즈
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점

# test case
test_case_len = int(input())
test_case = []


for i in range(test_case_len) :
    ox = str(input())
    test_case.append(ox)

# score calculate
for calc in test_case :
    # score count
    score = 0 # O를 만날 때마다 증가할 값. X만나면 초기화
    total_score = 0 # 하나의 test_case의 점수. 출력할 값
    for i in calc :
        if i == "X" :
            score = 0
        if i == "O" :
            score += 1
            total_score += score
    print(total_score)




