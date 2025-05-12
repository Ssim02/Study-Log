numbers = [1,2,3,4,5,6]

# map(함수, 리스트) -> 새로운 리스트를 만들어줌, lambda식을 사용해서 한 줄로 바로 새로운 문자열 리스트 생성. 
# str() -> 숫자를 문자열로 변환하는 함수
print("::".join(map(lambda x: str(x), numbers)))
