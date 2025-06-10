#  스택 구현

class Stack :
    def __init__(self) : # 생성 함수
        self.items = []
    
    def push(self, val) : # push
        self.items.append(val)
    
    def pop(self) : # pop
        try :
            return self.items.pop()
        except IndexError : # 스택에 남아있는 아이템이 없다면
            print("Stack is empty")
    
    def top(self) : # pop과는 다르게 요소를 제거하지는 않는다
        try :
            return self.items[-1]
        except IndexError :
            print("Stack is empty")
    
    def __len__(self) :
        return len(self.items)
    
    def isEmpty(self) :
        return len(self) == 0
