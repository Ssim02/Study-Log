# 백준 10989번 - 수 정렬하기 3

import sys

# 수의 개수 N 입력
N = int(sys.stdin.readline())

# 스택 구현
class Stack :
    def __init__(self) : # 생성 함수
        self.items = []
    def push(self, val) : # push 연산
        self.items.append(val)
    def pop(self) : # pop 연산
        try :
            return self.items.pop()
        except IndexError :
            return -1 # Stack is empty
    def top(self) : # top 연산
        try :
            return self.items[-1]
        except IndexError :
            return -1 # Stack is empty
    def __len__(self) :
        return len(self.items)
    def isEmpty(self) :
        return len(self) == 0

# 스택 인스턴스 생성
ascending_stack = Stack() # 오름차순으로 저장할 스택


# N개의 수를 한 줄씩 입력받고, 스택에 저장
for i in range(N) :
    n = int(sys.stdin.readline()) # 수 입력
    # 2025.06.23 - 여기까지 진행

