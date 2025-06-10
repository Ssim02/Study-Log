# 스택 구현

class Stack :
    def __init__(self) : # 생성 함수
        self.items = []

    def push(self, val) : # push X 처리
        self.items.append(val)

    def pop(self) : # pop 처리
        try :
            print(self.items.pop())
        except IndexError : # 스택이 비어있는 경우
            print(-1)

    def __len__(self) : # size 처리
        print(len(self.items))

    def empty(self) : # empty 처리
        if len(self.items) == 0 :
            print(1)
        else :
            print(0)
    def top(self) : # top 처리
        try :
            print(self.items[-1])
        except IndexError :
            print(-1)

# 반복할 횟수 입력
N = int(input())
stack = Stack() # 인스턴스 생성
# N만큼 반복하며, 주어진 입력에 따른 연산 처리값 출력
for i in range(N) :
    calc_input = list(map(str, input().split())) # push X 형태의 입력을 대응하기 위해
    
    real_calc = calc_input[0]

    # 각 입력에 따른 연산값 출력시키기
    if real_calc == "push" :
        stack.push(calc_input[1])
    elif real_calc == "pop" :
        stack.pop()
    elif real_calc == "size" :
        stack.__len__()
    elif real_calc == "empty" :
        stack.empty()
    elif real_calc == "top" :
        stack.top()
