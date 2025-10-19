# 백준 28278번 - 스택 2

# 스택 구현

class Stack :
    def __init__(self) : # 생성 함수
        self.items = []

    def push(self, val) : # 1번 명령
        self.items.append(val)

    def pop(self) : # 2번 명령
