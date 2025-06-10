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
            print(-1)

    def __len__(self) : # size 처리
        return len(self.items)

    def empty(self) : # empty 처리
        return len(self) == 0
    
    def top(self) : # top 처리
        try :
            return self.items[-1]
        except IndexError :
            print(-1)

# 반복할 횟수 입력
N = int(input())

# N만큼 반복하며, 주어진 입력에 따른 연산 처리값 출력
for i in range(N) :
    calc_input = map(str, input().split()) # push X 형태의 입력을 대응하기 위해
    for j in range(len(calc_input)) : # map에 인덱스로 접근 불가 -> for루프로 하나씩 접근해 각 요소를 새 변수에 저장하기?
        real_calc = j # 밑 부분의 calc_input[0] 을 전부 이 변수로 변경해서 대입
        break # 어짜피 [0]만 필요하므로 루프 탈출
    # 각 입력에 따른 연산값 출력시키기
    if calc_input[0] == "push" :
        Stack.push(calc_input[1])
    elif calc_input[0] == "pop" :
        Stack.pop()
    elif calc_input[0] == "size" :
        Stack.__len__()
    elif calc_input[0] == "empty" :
        Stack.empty()
    elif calc_input[0] == "top" :
        Stack.top()
