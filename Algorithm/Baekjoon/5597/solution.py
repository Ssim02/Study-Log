# 백준 5597번 - 과제 안 내신 분..?

# 1~30이 저장된 리스트 만들기
attendance_number = []
for i in range(30) :
    attendance_number.append(i + 1)

# 입력 받고, 입력받은 수를 리스트에서 제거
for i in range(28) :
    n = int(input())
    if(n in attendance_number) :
        attendance_number.remove(n) 


# 입력되지 않은 나머지 두 수 출력
print(attendance_number[0])
print(attendance_number[1])
