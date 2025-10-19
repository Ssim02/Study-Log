# 단어의 개수를 체크할 변수
count = 0
# 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어짐. 
s = input()

# split 이용해서 단어로 쪼개기기
words= s.split()

# 루프 돌면서 단어의 개수 카운트
for i in range(len(words)) :
    count += 1
# 단어의 개수를 출력
print(count)