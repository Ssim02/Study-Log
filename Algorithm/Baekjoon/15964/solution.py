# 백준 15964 - 이상한 기호

def sub(a, b) :
    res = (a+b)*(a-b)
    return res


a, b = map(int, input().split())

print(sub(a, b))
