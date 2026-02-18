numbers = [1, 2, 3, 4]

# 1
squares = list(map(lambda x: x * x, numbers))

# 2
cubes = list(map(lambda x: x ** 3, numbers))

# 3
plus_two = list(map(lambda x: x + 2, numbers))

# 4
strings = list(map(lambda x: "Num:" + str(x), numbers))

print(squares)
print(cubes)
print(plus_two)
print(strings)
