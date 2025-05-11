# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램

number = [] # 입력받은 수를 저장할 리스트
mod = [] # 계산한 나머지를 저정할 리스트
count = 1 # 서로 다른 값이 있는 개수를 체크할 변수
# 10개의 수 입력받기
for i in range(10) :
    i = int(input())
    number.append(i)

# 42로 나눈 나머지를 리스트에 저장
for i in range(10) :
    mod.append(number[i] % 42)

# 구한 나머지 중 서로 다른 값이 몇 개 있는지를 구함
for i in range(9) :
    if mod[i] != mod[i + 1] :
        count += 1     

print(count)
