# infix 수식을 postfix수식으로 변경하고, 실제 계산까지 처리하는 프로그램입니다.

# Stack 정의

class Stack : 
    def __init__(self) : # 생성 함수
        self.items = []

    def push(self, val) : # push 연산을 수행
        self.items.append(val) 
    
    def pop(self) : # pop연산을 수행
        try :
            return self.items.pop()
        except IndexError :
            print("Stack is empty")
    
    def top(self) : # top연산을 수행
        try :
            return self.items[-1]
        except IndexError :
            print("Stack is empty")
    
    def __len__(self) :
        return len(self.items)

    def is_empty(self) :
        return len(self) == 0


# 연산자 우선순위를 저장하기 위한 딕셔너리
prec = {
    '*' : 3, '/' : 3,
    '+' : 2, '-' : 2,
    '(' : 1
}

# 입력받은 수식(문자열)을 의미 있는 최소 단위(토큰)으로 나누기 위한 토크나이징 함수

def tokenize_expression(expression) :
    # 공백 없는 수식 문자열을 숫자와 기호 토큰으로 분리하여 리스트로 반환
    tokens = []
    current_number = ''

    # 입력된 수식 문자열을 한 글자씩 순회
    for char in expression :
        # 1. 현재 글자가 숫자인 경우
        if char.isdigit() or char == '.' : # 소수점도 숫자의 일부로 처리
            current_number += char
        # 2. 현재 글자가 기호인 경우
        else :
            # 이전에 완성된 숫자가 있다면, 리스트에 추가하고 초기화
            if current_number :
                # 숫자로 변환 (정수 또는 실수)
                try :
                    tokens.append(int(current_number))
                except ValueError :
                    tokens.append(float(current_number))
                current_number = '' # 초기화

            # 현재 기호를 리스트에 추가
            tokens.append(char)

    # 3. 루프가 끝난 후, 마지막에 숫자가 남아있는 경우 처리
    if current_number :
        try :
            tokens.append(int(current_number))
        except ValueError :
            tokens.append(float(current_number))

    return tokens


# infix 수식을 입력받는다
infix_expression = input("")

# 토크나이징 함수를 호출하여 결과를 받음
infix_tokens = tokenize_expression(infix_expression)

# postfix 수식으로 변환시키기
def infix_to_postfix(infix_tokens) :
    postfix_list = [] # postfix로 변환한 수식을 저장할 리스트
    opstack = Stack() # 수식 변환과정중 사용할 스택

    for token in infix_tokens :
        if isinstance(token, (int, float)) : # token이 피연산자라면
            postfix_list.append(token)
        if token == '(' : # 왼쪽 괄호 - 오른 괄호를 만나기 전까지는 그냥 push        
            opstack.push(token)
        if token == ')' : # 오른 괄호 - 스택 내부의 왼쪽 괄호를 pop할때까지 스택의 요소들을 모두 pop
            while True :
                op = opstack.pop() # 스택에서 연산자를 하나 꺼냄
                if op == '(' : # 꺼낸 연산자가 '('이면
                    break # 루프 중단
                # '('가 아니라면, 다른 연산자이므로 postfix에 추가
                postfix_list.append(op)
        if token in '+*-/' : 
            # 스택의 top에 있는 연산자가 현재 연산자보다 우선순위가 높거나 같으면 pop
            while not opstack.is_empty() and prec[opstack.top()] >= prec[token] :
                postfix_list.append(opstack.pop())
            # 현재 연산자를 스택에 push
            opstack.push(token)

    # 루프가 끝난 후 스택에 남아있는 모든 연산자를 리스트에 추가
    while not opstack.is_empty() :
        postfix_list.append(opstack.pop())

    return postfix_list

# postfix로 변환된 수식을 계산하는 함수
def postfix_calc(postfix_list) :
    for token in postfix_list :
        if isinstance(token, (int, float)) :
            # 2025.06.19 여기까지

