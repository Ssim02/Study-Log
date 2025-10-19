# 백준 2744번 - 대소문자 바꾸기

# 입력
word = input()
# 바꾼 결과를 저장할 문자열
res = ''
# 대소문자 변환
for i in word :
    if i.isupper() :
        res += i.lower()
    if i.islower() :
        res += i.upper()
# 출력
print(res)
