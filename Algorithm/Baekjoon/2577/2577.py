# 2577번 : 숫자의 개수
# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

res = a * b * c

str_res = str(res)

# 숫자가 몇 번 쓰였는지 저장할 딕셔너리 생성
res_dict = {
    "0" : 0,
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0,
}

# 곱셈의 결과에 0부터 9까지의 숫자가 각각 몇 번쓰였는지 차례로 한 줄에 하나씩 출력

# 루프를 돌며 곱셈의 결과의 숫자의 개수를 딕셔너리의 해당 키에 요소에 카운트
for i in str_res :
    if i in res_dict :
        res_dict[i] += 1

# 출력
for i in res_dict :
    print(res_dict[i])



