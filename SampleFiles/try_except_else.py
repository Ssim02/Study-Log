# try except else 구문으로 예외를 처리
try:
    number_input_a = int(input("정수 입력>"))
except:
    print("정수를 입력하지 않았습니다")
else:
    # 예외가 발생하지 않았을 경우에 출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 3.14 * 2 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
