def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

# map()
output_a = map(power, list_input_a) # 함수를 매개변수로 넣는다
print("# map() function result")
print("map(power, list_input_a):", output_a) # 제너레이터가 출력됨
print("map(power, list_input_a):", list(output_a)) # 리스트 자료형으로 변환해 출력
print()

# filter()
output_b = filter(under_3, list_input_a) # 함수를 매개변수로 넣는다
print("# filter() function result")
print("filter(under_3, list_input_a):", output_b) # 제너레이터가 출력됨
print("filter(under_3, list_input_a):", list(output_b)) # 리스트 자료형으로 변환해 출력
