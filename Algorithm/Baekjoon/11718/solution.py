# 백준 11718 - 그대로 출력하기

# 예외 처리 이용해서 풀이

while(True) :
    try :
        n = input()
        print(n)
    except EOFError:
        break
