import sys

# 스택 구현

class Stack :
    def __init__(self) : # 생성 함수
        self.items = []

    def push(self, val) : # push X 처리
        self.items.append(val)

    def pop(self) : # pop 처리
        try :
            return self.items.pop()
        except IndexError : # 스택이 비어있는 경우
            return -1

    def __len__(self) : # size 처리
        return len(self.items)

    def empty(self) : # empty 처리
        if len(self.items) == 0 :
            return 1
        else :
            return 0
   
    def top(self) : # top 처리
        try :
            return self.items[-1]
        except IndexError :
            return -1

# 반복할 횟수 입력
N = int(sys.stdin.readline().rstrip())

stack = Stack() # 인스턴스 생성
res_list = [] # 출력값을 저장해둘 리스트

# N만큼 반복하며, 주어진 입력에 따른 연산 처리 후 리스트에 저장
for i in range(N) :
    calc_input = list(map(str, input().split())) # push X 형태의 입력을 대응하기 위해
    
    real_calc = calc_input[0]

    # 각 입력에 따른 연산값 출력시키기
    if real_calc == "push" :
        stack.push(calc_input[1])
    elif real_calc == "pop" :
        res_list.append(stack.pop())
    elif real_calc == "size" :
        res_list.append(stack.__len__())
    elif real_calc == "empty" :
        res_list.append(stack.empty())
    elif real_calc == "top" :
        res_list.append(stack.top()) 

# 리스트에 저장한 출력값들 내보내기
for i in res_list :
    print(i)
