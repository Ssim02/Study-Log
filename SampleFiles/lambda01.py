# 람다로 함수 선언
power = lambda x: x * x
under_3 = lambda x: x < 3

# 변수 선언
list_input_a = [1,2,3,4,5]

# use map()
output_a = map(power, list_input_a)
print("# map() result")
print("map(power, list_input_a):", output_a) # result is generator
print("map(power, list_input_a):", list(output_a))
print()

# use filter()
output_b = filter(under_3, list_input_a)
print("# filter() result")
print("filter(under_3, list_input_a):", output_b) # result is generator
print("filter(under_3, list_input_a):", list(output_b))
