# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램

mod = [] # 계산한 나머지를 저정할 리스트

# 10개의 수 입력받고 42로 나눈 값을 mod에 저장
for i in range(10) :
    num = int(input())
    mod.append(num % 42)
   
# 중복 제거 후 길이 출력
print(len(set(mod)))
