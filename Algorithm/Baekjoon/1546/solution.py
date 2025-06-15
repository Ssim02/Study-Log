# 백준 1546번 - 평균

# 시험을 본 과목의 개수 N 입력
N = int(input())

# 현재 성적을 입력
now_score_list = list(map(int, input().split()))
new_score_list = [] # 새로운 성적을 저장할 리스트

# 성적 중 최고점을 구하기
max_score = 0
for i in now_score_list :
    if i > max_score :
        max_score = i   


# 새로운 점수 구하기
for i in now_score_list :
    new_score_list.append(i / max_score * 100)

# 새로운 평균 구하기
avg = 0
for i in new_score_list :
    avg += i

# 새로 구한 평균을 출력
print(avg/len(now_score_list))
