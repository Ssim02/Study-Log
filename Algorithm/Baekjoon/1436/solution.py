# 백준 1436번 - 영화감독 숌

# 입력
N = int(input())
count = 0
num = 666

# 출력
while True :
    if '666' in str(num) :
        count += 1 # 666이 들어가 있으면 count ++
        if count == N : # 조건에 맞는 수이면 출력
            print(num)
            break
    num += 1 # 666이 들어가지 않았을 경우에 계속 진행해야 하므로 num += 1을 해준다다

