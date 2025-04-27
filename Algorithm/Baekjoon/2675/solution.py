# 테스트 케이스 입력받기
test_case_number= int(input())
r_array = []
s_array = []

for i in range(test_case_number) :
    r, s = input().split() # 반복횟수 r과 문자열 s을 공백을 기준으로 입력받음
    r_array.append(r)
    s_array.append(s)

# i번째 문자 r번 반복 출력
for i in range(len(r_array)) :
    for sub_i in s_array[i] :
        print(sub_i * int(r_array[i]), end = "") # 줄바꿈 생략
    print()
 