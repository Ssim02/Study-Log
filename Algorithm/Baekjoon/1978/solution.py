# 백준 1978번 - 소수 찾기

# 수의 개수 N 입력
N = int(input())

# N개의 수 입력
# 슬라이싱으로 N개의 수만 입력되도록 강제제한
numbers = list(map(int, input().split())) [:N]

# 입력값에서 소수가 몇 개인지 구하기
count = 0 # 소수의 개수를 체크할 변수
# 소수 판정법 - 2부터 루트n까지 나누어 나누어떨어지는 게 있으면 소수가 x
# 루트 n 구하기 - (n**(1/2))
# 중간에 flag를 세워 소수 판정이 완료되었을 때 한번만 count += 1을 수행하도록 해야함함
for i in numbers :
    if i == 1 :
        continue # 1은 소수가 아니므로로
    flag = 0 # 지금은 소수가 아니다
    for j in range(2, int(i**(1/2) + 1)) :
        if i % j == 0 :
            flag = 1 # 나누어 떨어지는 수가 존재 - 현재 i는 합성수이다.
            break
    if flag == 0 :
        count += 1 # 루프를 빠져나왔는데 나누어 떨어지는 수가 존재하지 않음. 현재 i는 소수이다다        
print(count)
