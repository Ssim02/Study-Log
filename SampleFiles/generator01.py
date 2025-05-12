# 함수를 선언
def test() :
    print("pass the a-branch")
    yield 1
    print("pass the b-branch")
    yield 2
    print("pass the c-branch")
# 함수를 호출
output = test()
# next()함수를 호출
print("pass the d-branch")
a = next(output)
print(a)
print("pass the e-branch")
b = next(output)
print(b)
print("pass the f-branch")
c = next(output)
print(c)
# 한번 더 실행하기
next(output)
