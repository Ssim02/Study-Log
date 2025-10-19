# 백준 2231번 - 분해합

# 분해합을 입력받는다
N = int(input())

# 루프를 돌아 생성자를 찾는다. 생성자가 없는 경우에는 0을 출력한다

for i in range(1, N + 1) :
   digits = list(map(int, str(i))) # 하나씩 잘라서 저장
   print("{} -> {}".format(i, digits)) # 확인용 출력
   # 잘라서 저정한 후 분해합인지를 검사
   # a, b, c -> abc + a + b + c = i이면 분해합 성립
   #for j in digits :
      
