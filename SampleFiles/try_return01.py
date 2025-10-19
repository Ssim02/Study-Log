def test():
    print("test() 함수의 첫 번째 줄")
    try:
        print("try 구문이 실행됨")
        return # try 구문 중간에 탈출
        print("try 구문의 return 키워드 뒤임")
    except:
        print("except구문이 실행됨")
    else:
        print("else 구문이 실행됨")
    finally:
        print("finally 구문이 실행됨") # try 구문 중간에 탈출해도, finally 구문은 무조건 실행된다.
    print("test()함수의 마지막 줄")


test()
