sum = 0
for i in range(1, 10 + 1) :
    sum += i

sum = sum(i for i in range(1, 10 + 1))

sum = sum(range(1, 10 + 1))
